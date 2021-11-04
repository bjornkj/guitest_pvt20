import pytest


# From https://stackoverflow.com/questions/60205391/how-to-capture-screenshot-on-test-case-failure-with-pytest
# https://github.com/rafitur2/Python-Pytest-Selenium-HTML-report-with-multiple-screenshots/blob/master/conftest.py

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()

    extra = getattr(report, "extra", [])

    if report.when == "call":
        if report.failed:
            # report.nodeid är namnet på vårt test på formen pythonfil.py::testfunktion
            file_name = f"screenshots/{report.nodeid.replace('::', '__')}.png"
            # file_name skall vi använda när vi skapar html-taggen för att få in skärmdumpen vi just tog i rapporten
            # I rapporten behöver vi ange sökvägen till skärmdumpen, en relativ sökväg så exempelvis
            # screenshots/mitt_test.png
            html_report_path = "reports/html_reports/"
            # För att ta en skärmdump måste vi få tag på en referns till webdrivern som används i testet
            # i våra tester får vi wedrivern som ett argument kallat browser
            browser = item.funcargs['browser']
            browser.save_screenshot(html_report_path + file_name)
            extra.append(pytest_html.extras.html(create_img_tag(file_name)))
        report.extra = extra


def create_img_tag(file_path):
    return f'<div class="image"><a href="{file_path}"><img ' \
           f'src="{file_path}"/></a></div>'\


# TODO lägg till något mer i filnamnen så att om vi kör samma test med olika webläsare skall inte skärmdumpar skrivas över
# Man kan t.ex. använda en tidsstämpel i filnamnet
# TODO se till att man skapar en ny underkatalog för rapporterna vid varje körning
# ex: reports/test_run_20211104_154515/html_report/

# För att köra alla tester och generera en html-rapport
# pytest  --html=reports/html_reports/report.html
# för xml-output
# pytest  --html=reports/html_reports/report.html
# Eller båda
# pytest  --html=reports/html_reports/report.html