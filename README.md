# bench-pytorch

Scripts and configuration to run the [PyTorch](https://pytorch.org/) benchmark within the [crucible](https://github.com/perftool-incubator/crucible) performance testing framework.

See `run-pytorch.json` for example usage with `crucible run run-pytorch.json`.

## Key Files

| File | Purpose |
|------|---------|
| `rickshaw.json` | Rickshaw integration: defines client scripts and parameter transformations |
| `multiplex.json` | Parameter validation and presets for multiplex |
| `pytorch-base` | Base setup shared by other scripts |
| `pytorch-client` | Client-side benchmark execution |
| `pytorch-get-runtime` | Runtime extraction |
| `pytorch-post-process` | Post-processing: parses pytorch output into crucible metrics |
| `workshop.json` | Engine image build requirements |
