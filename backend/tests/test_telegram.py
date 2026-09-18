1s
Run pytest tests/test_telegram.py -v
  pytest tests/test_telegram.py -v
  shell: /usr/bin/bash -e {0}
  env:
    pythonLocation: /opt/hostedtoolcache/Python/3.12.14/x64
    PKG_CONFIG_PATH: /opt/hostedtoolcache/Python/3.12.14/x64/lib/pkgconfig
    Python_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.14/x64
    Python2_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.14/x64
    Python3_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.14/x64
    LD_LIBRARY_PATH: /opt/hostedtoolcache/Python/3.12.14/x64/lib
    PYTHONPATH: .
============================= test session starts ==============================
platform linux -- Python 3.12.14, pytest-9.1.1, pluggy-1.6.0 -- /opt/hostedtoolcache/Python/3.12.14/x64/bin/python
cachedir: .pytest_cache
rootdir: /home/runner/work/IranStockAnalyzer/IranStockAnalyzer/backend
plugins: anyio-4.15.1
collecting ... collected 1 item

tests/test_telegram.py::test_telegram_chart_command FAILED               [100%]

=================================== FAILURES ===================================
_________________________ test_telegram_chart_command __________________________

monkeypatch = <_pytest.monkeypatch.MonkeyPatch object at 0x7fa53d1eae70>

    def test_telegram_chart_command(monkeypatch):
        fake_history = [
            {
                "date": "2026-09-18",
                "open": 1000,
                "high": 1100,
                "low": 900,
                "close": 1050,
            }
        ]
    
        def fake_get_history(self, symbol):
            return fake_history
    
        monkeypatch.setattr(
            "app.services.market_data_service.MarketDataService.get_history",
            fake_get_history,
        )
    
>       response = client.get("/telegram/command/%2Fchart%20NOURI")
                   ^^^^^^
E       NameError: name 'client' is not defined

tests/test_telegram.py:20: NameError
=========================== short test summary info ============================
FAILED tests/test_telegram.py::test_telegram_chart_command - NameError: name 'client' is not defined
============================== 1 failed in 0.12s ===============================
Error: Process completed with exit code 1.
