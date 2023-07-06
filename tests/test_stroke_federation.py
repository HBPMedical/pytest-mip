import time
import pytest
from basetest import BaseMIPFederationTest
from selenium.webdriver.common.by import By


"""
This pytest test is dedicated to interactively test the MIP Stroke (FERES) federation.

    Project: Test of the MIP federations
    Test: Stroke (FERES)
    Created by: Sebastien Tourbier (sebastien.tourbier@chuv.ch)
    Created on 06/07/2023
    Modified by: Sebastien Tourbier (sebastien.tourbier@chuv.ch)
    Last modification: 06/07/2023

"""

FEDERATION_URL = "https://stroke.hbpmip.link/"


@pytest.mark.parametrize("selenium_driver", [FEDERATION_URL], indirect=True)
class TestStrokeMIP(BaseMIPFederationTest):
    def test_login_and_accept_terms(self):
        """Test login and accept terms on the Stroke (FERES) MIP."""
        super().test_login_and_accept_terms()

    def test_data(self):
        """Integration tests (data) of the Stroke (FERES) MIP."""
        selenium_driver = self.driver

        # 1. Click 'Datasets'
        datasets = selenium_driver.find_element(By.CSS_SELECTOR, "#dropdown-basic")
        datasets.click()

        # 2. Disable and enable again 'default-unibas'
        time.sleep(3)
        default_unibas_wk = selenium_driver.find_element(
            By.CSS_SELECTOR, "#default-unibas"
        )
        default_unibas_wk.click()
        default_unibas_wk.click()

        # 3. Click 'age'
        age = selenium_driver.find_element(
            By.XPATH,
            "//*[name()='circle'][590]",
        )
        age.click()

        # 4. Is the div containing the histogram of 'age' generated?
        histogram_of_age = selenium_driver.find_element(
            By.XPATH,
            "//div[contains(@id,'bar-graph-age')]",
        )
        assert histogram_of_age

        # 5. Click 'nihss 24h'
        nihss_24h = selenium_driver.find_element(
            By.XPATH,
            "//*[name()='circle'][499]",
        )
        nihss_24h.click()

        # 6. Is the div containing the histogram of 'nihss 24h' generated?
        histogram_of_nihss_24h = selenium_driver.find_element(
            By.XPATH,
            "//div[contains(@id,'bar-graph-nihss-24h')]",
        )
        assert histogram_of_nihss_24h

        # 7. Click 'sbp admiss'
        sbp_admiss = selenium_driver.find_element(By.XPATH, "//*[name()='circle'][581]")
        sbp_admiss.click()

        # 8. Is the div containing the histogram of 'age' generated?
        histogram_of_sbp_admiss = selenium_driver.find_element(
            By.XPATH,
            "//div[contains(@id,'bar-graph-sbp-admiss')]",
        )
        assert histogram_of_sbp_admiss
