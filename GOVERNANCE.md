# Project governance

LockedIn Labs maintains this organization. Repository maintainers own technical decisions within their project's documented scope; organization owners manage membership, repository settings, and publication authority.

## Changes and decisions

Use issues to describe a problem and pull requests to propose a concrete change. Material interface, security, storage, or deployment changes should include the relevant architectural decision, migration/compatibility implications, and failure behavior. Maintainers decide acceptance based on correctness, security, maintainability, and fit with the project.

Keep product-specific instructions in the product repository. These community defaults apply where a repository has not defined a more specific process.

## Releases

Publish from a reviewed commit after the repository's checks pass. Record the version, changes, installation path, and verification instructions. Follow the [public release standard](RELEASE-STANDARD.md), including full-history review and owner authorization before the first public publication. An experimental interface must be identified as such.

An upstream contribution and a company-maintained distribution should identify their relationship clearly. Keep attribution and license notices, identify the canonical issue and release locations, and avoid parallel packages with indistinguishable names or versions.

## Access and maintenance

Grant access for a defined role and use the least permission that supports it. Protect release branches, review permission changes, and keep release credentials separate from ordinary contributions. Documentation describes the intended practice; each repository's settings and release evidence establish which controls are active.

If maintenance changes, update the README and support policy. Archived projects remain useful references when their status and supported versions are clear.
