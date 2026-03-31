# Bench-pytorch

## Purpose
Scripts and configuration to run the PyTorch benchmark within the crucible framework.

## Language
Bash — all scripts

## Key Files
| File | Purpose |
|------|---------|
| `rickshaw.json` | Rickshaw integration: client scripts, parameter transformations |
| `multiplex.json` | Parameter validation and presets for multiplex |
| `pytorch-base` | Base setup shared by other scripts |
| `pytorch-client` | Client-side benchmark execution |
| `pytorch-get-runtime` | Extracts runtime from command-line options |
| `pytorch-post-process` | Parses pytorch output into crucible metrics |
| `workshop.json` | Engine image build requirements |

## Conventions
- Primary branch is `main`
- Standard Bash modelines and 4-space indentation
