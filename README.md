# herdr-smoketest

A minimal smoke test for confirming that a host is alive, reachable, and running
the expected environment. `prove.py` prints a small JSON fingerprint of the
machine it runs on: hostname, CPU architecture, Python version, and a UTC
timestamp.

## Usage

```bash
python3 prove.py
```

Example output:

```json
{
  "hostname": "pa-joshi-MacBookPro9-2",
  "arch": "x86_64",
  "python_version": "3.14.4 (main, Aug 20 2026, 10:41:58) [GCC 15.2.0]",
  "timestamp_utc": "2026-09-19T01:01:39.874228+00:00"
}
```

## Files

- `prove.py` — the smoke test script.
- `run1.json`, `run2.json` — two sample runs captured ~90 seconds apart,
  demonstrating that the timestamp advances and the rest of the fingerprint
  stays stable across runs on the same host.
