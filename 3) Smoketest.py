from unittest import TestLoader, TestSuite
from HtmlTestRunner import HTMLTestRunner
from searchtest import find_elements
from assertion_and_suite_test import assertion_test

assertions_test = TestLoader().loadTestsFromTestCase(assertion_test)
search_test = TestLoader().loadTestsFromTestCase(find_elements)

smoke_test = TestSuite([assertions_test, search_test])

kwargs = {
    "output": "reports/smoke-report",
    "report_name": "smoke-report",
    "combine_reports": True,
    "add_timestamp": False
}


runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)