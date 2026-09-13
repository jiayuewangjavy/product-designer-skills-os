# Security

## Package boundary

The v0 repository contains Markdown skill instructions, UI metadata, references, one image, and a local static validator. It does not vendor third-party skills, execute network requests, request credentials, or include installation automation.

Treat any future external dependency, script, MCP server, browser automation, or publishing action as a new security surface. Review it before adding it to a default profile.

## Reporting

Open a GitHub issue for prompt-injection risks, unsafe side effects, misleading authorization, dependency concerns, exposed secrets, or license/provenance problems. Do not include real credentials, private product data, or exploit details that would put users at immediate risk.

## Release checks

- scan for secrets and machine-local paths;
- validate every skill and metadata file;
- review scripts, network access, and mutation boundaries;
- pin and recheck external source commits and licenses;
- confirm no third-party implementation was copied without compatible terms;
- verify that planning or drafting skills do not imply authorization to publish, message, charge, delete, or deploy.
