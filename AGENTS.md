# Bench-pytorch

## Purpose
Scripts and configuration to run the PyTorch benchmark within the crucible framework.

## Language
- Bash for client execution scripts
- Python for post-processing (`pytorch-post-process`)

## Key Files
| File | Purpose |
|------|---------|
| `rickshaw.json` | Rickshaw integration: client scripts, parameter transformations |
| `multiplex.json` | Parameter validation rules, unit conversions, and presets for multiplex |
| `benchmark-metadata.json` | Machine-readable description and CDM-indexed source/type list (consumed by `crucible benchmarks list`) |
| `pytorch-base` | Base setup shared by other scripts |
| `pytorch-client` | Client-side benchmark execution |
| `pytorch-get-runtime` | Extracts runtime from command-line options |
| `pytorch-post-process` | Parses pytorch output into crucible metrics |
| `workshop.json` | Engine image build requirements |

## Conventions
- Primary branch is `main`
- Standard Bash modelines and 4-space indentation
- Python code follows 4-space indentation with standard modelines
