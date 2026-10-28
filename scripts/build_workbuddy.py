#!/usr/bin/env python3
"""Build one self-contained WorkBuddy skill from the canonical skill network."""
from pathlib import Path
import argparse
import json
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / 'workbuddy' / 'product-designer-skills-os'
NAMES = {
    'product-design-router': '产品设计路由',
    'product-context': '产品上下文',
    'opportunity-and-assumption-map': '机会与假设地图',
    'conceptual-model-design': '概念模型设计',
    'prototype-question': '原型验证问题',
    'interactive-prototype': '交互原型',
    'design-judgment-scorecard': '设计判断评分',
    'intent-preservation-check': '产品意图检查',
    'position-and-launch-hypothesis': '定位与发布假设',
    'learning-loop-readout': '学习闭环复盘',
}

def render():
    files = {}
    rows = []
    for name, label in NAMES.items():
        source = ROOT / 'skills' / name
        text = (source / 'SKILL.md').read_text(encoding='utf-8')
        body = text.split('---', 2)[2].strip()
        # References in a flattened instruction file must remain inside this package.
        body = re.sub(r'\]\(references/([^)]+)\)',
                      lambda m: f']({name}/{m[1]})', body)
        files[f'references/{name}.md'] = body + '\n'
        for ref in sorted((source / 'references').glob('**/*')):
            if ref.is_file():
                files[f'references/{name}/{ref.relative_to(source / "references").as_posix()}'] = ref.read_text(encoding='utf-8')
        rows.append(f'- {label}（`{name}`）：@references/{name}.md')
    files['references/LOOP-CONTRACT.md'] = (ROOT / 'references/LOOP-CONTRACT.md').read_text(encoding='utf-8')
    files['LICENSE'] = (ROOT / 'LICENSE').read_text(encoding='utf-8')
    metadata = {
        'name': 'product-designer-skills-os',
        'display_name': '产品设计 Skills OS',
        'display_name_en': 'Product Designer Skills OS',
        'description': '产品设计与独立产品构建：判断下一步、整理上下文、梳理假设、概念模型、原型验证、交互原型、设计评审、意图检查、定位发布及复盘。用户明确指定任务时直接执行相应能力。',
        'description_zh': '以最高风险未知驱动的产品设计与学习闭环。',
        'description_en': 'An uncertainty-driven product design and learning skill network.',
        'version': '0.1.0',
        'author': 'jiayuewangjavy',
    }
    frontmatter = '\n'.join(f'{key}: {json.dumps(value, ensure_ascii=False)}' for key, value in metadata.items())
    files['SKILL.md'] = '---\n' + frontmatter + '\n---\n\n' + '''# Product Designer Skills OS · WorkBuddy

## 使用方式

默认按用户语言回复。保留原始技能中的方法、证据边界和决策责任。
此整合包已包含全部 10 个能力；它们是包内参考指令，不依赖另行安装的技能、Codex 插件、`$skill-name` 语法或特定 MCP 工具。

- 用户明确提出原型、评审、复盘等任务：只读取对应能力文件并执行，不强制经过完整流程。
- 用户不知道下一步做什么：先读取 @references/product-design-router.md，按最高风险未知选择一个主能力，必要时最多两个支持能力。
- 选中能力后读取下方对应文件；不要只报技能名称就结束。文件内的“调用 / route to”表示读取并应用本包对应指令，不是调用不存在的工具。
- 需要跨能力闭环时读取 @references/LOOP-CONTRACT.md；不要一次性加载所有资料。
- 参考指令含英文时，按其含义执行并用用户语言交付，不要求用户懂英文。

## 能力索引

''' + '\n'.join(rows) + '''

## WorkBuddy 执行约定

- 只使用当前会话实际可用的文件、浏览、代码执行或连接器能力。先检查已有附件和工作区；不得假装已访问 Figma、GitHub、分析后台或其他服务。
- 相对链接以所属参考文件所在目录解析；补充资料已包含在本包的 references 目录内。
- 复用已有产品上下文；无既有文件且允许写入时，使用工作区中的 `.agents/product-context.md`。无法写文件时在对话提供可复制的 Markdown，并明确尚未保存。
- 交互原型优先复用项目现有实现；无项目时可用无外部依赖的 HTML/CSS/JavaScript。无代码执行能力时提供可保存的代码、操作说明及“尚未运行验证”的限制。
- 模拟数据、假设和真实观察分开标注。生成原型不等于验证了需求；没有参与者测试时不得宣称通过可用性验证。
- 跨会话不假定自动记忆。输出已知、产出、学到什么、决策变化、下一个未知，供用户保存并在下一会话提供。
- 仍按用户已授权范围执行；不把 workshop 练习视为授权发布、发消息、付款、删除或修改线上系统。
'''
    return files

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Fail if committed generated files differ from sources')
    args = parser.parse_args()
    files = render()
    if args.check:
        actual = {p.relative_to(TARGET).as_posix(): p.read_text(encoding='utf-8') for p in TARGET.rglob('*') if p.is_file()}
        if actual != files:
            raise SystemExit('WorkBuddy package is stale; run python scripts/build_workbuddy.py')
        for relative, content in files.items():
            if not relative.endswith('.md'):
                continue
            for link in re.findall(r'\]\(([^)]+)\)', content):
                if '://' not in link and not link.startswith('#'):
                    resolved = (TARGET / relative).parent / link
                    if not resolved.is_file() or not resolved.resolve().is_relative_to(TARGET.resolve()):
                        raise SystemExit(f'Missing or external reference: {relative}: {link}')
        for reference in re.findall(r'@([^\s；，。]+\.md)', files['SKILL.md']):
            if reference not in files:
                raise SystemExit(f'Missing entrypoint reference: {reference}')
        with zipfile.ZipFile(TARGET.with_suffix('.zip')) as bundle:
            expected = {f'{TARGET.name}/{key}': value.encode('utf-8') for key, value in files.items()}
            if set(bundle.namelist()) != set(expected) or any(bundle.read(key) != value for key, value in expected.items()):
                raise SystemExit('ZIP differs from generated package; rebuild it')
        print(f'PASS WorkBuddy: {len(NAMES)} capabilities, {len(files)} self-contained files')
        return
    TARGET.mkdir(parents=True, exist_ok=True)
    for old in TARGET.rglob('*'):
        if old.is_file() and old.relative_to(TARGET).as_posix() not in files:
            old.unlink()
    for relative, content in files.items():
        path = TARGET / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding='utf-8')
    archive = ROOT / 'workbuddy' / 'product-designer-skills-os.zip'
    with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as bundle:
        for relative, content in sorted(files.items()):
            info = zipfile.ZipInfo(f'{TARGET.name}/{relative}', date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            bundle.writestr(info, content.encode('utf-8'))
    print(f'Built {archive.relative_to(ROOT)}')

if __name__ == '__main__':
    main()
