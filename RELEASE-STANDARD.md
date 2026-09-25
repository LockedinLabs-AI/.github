# Public release standard

A public repository is an engineering product. A useful demonstration includes inspectable architecture, reproducible behavior, clear limits, and a maintained release path.

## Before first publication

1. Verify ownership and redistribution rights for code, data, fixtures, images, and dependencies. Preserve required licenses and attribution.
2. Review every reachable commit and packaged artifact. Exclude credentials, personal or customer data, machine-specific paths, private fixtures, prompts, session transcripts, internal handoffs, scratch files, and generated debris. Start a clean public history when the development history cannot be published; preserve the private source unchanged.
3. Document architectural boundaries, stable interfaces, supported runtimes, storage and identity adapters, installation, and the threat model. Keep shared domain/core code independent of product portals and integration adapters.
4. Verify least-privilege defaults, server-side authorization, validation, safe errors, and rate limits where applicable. Test relevant failure paths as well as the main example.
5. Include README, architecture and threat-model notes, contribution and security policies, license, third-party notices where needed, semantic versioning, changelog, and reproducible build/release instructions.
6. Run applicable CI for lint, type checks, tests, build, secrets, dependencies, and packaged artifacts. Documentation-only repositories need documentation and content checks rather than placeholder application tests.
7. Protect release branches. The owner reviews the exact sanitized candidate and authorizes the first public publication. Publish only from that reviewed commit.

## Each release

Identify the source revision, version, supported interfaces, compatibility changes, and known limits. Verify installation from the actual archive or package. Publish checksums and provenance when applicable, and link the release to its security advisory if it contains a disclosed fix.

Do not use passing tests, a hosted URL, a signed local artifact, or a synthetic demonstration as evidence of a broader production, regulatory, or independent certification claim. State what the evidence proves.
