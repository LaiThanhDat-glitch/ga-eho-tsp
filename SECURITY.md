# Security Policy

## Supported Versions

Security reports are considered for the current development version on the main branch. Older snapshots are provided for academic and research reference and are not covered by a separate maintenance commitment. This project does not guarantee a response time.

## Reporting a Vulnerability

Please do not report exploitable details, credentials, or personal information in a public issue.

If private vulnerability reporting is enabled for the repository, use the repository's **Security → Report a vulnerability** feature. Otherwise, contact the project lead privately through an established team contact. If you do not have a private contact route, open a public issue asking for one without describing the vulnerability.

Include the affected version or commit, relevant configuration, steps to reproduce, expected impact, and a minimal example. Remove secrets and sensitive data. Please coordinate public disclosure with the maintainer after the report has been reviewed and, where appropriate, addressed.

## Security Practices

- Run notebooks and code only when you trust their source; notebook cells can execute arbitrary Python code.
- Keep Jupyter bound to the local machine unless suitable authentication and network controls are configured.
- Do not commit credentials, private data, or local environment files.
- Review dependency changes and rerun the relevant project checks before relying on results.
