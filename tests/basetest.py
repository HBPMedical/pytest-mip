import time
import pytest
import project_parameters
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("selenium_driver")
class BaseMIPFederationTest:
    def test_login_and_accept_terms(self):
        """Test login and accept terms."""
        selenium_driver = self.driver
        """Log in to federation, accept the terms, and skip the introduction guide."""
        # 1. Click 'Login'
        login = selenium_driver.find_element(By.XPATH, "//button[. = 'Login']")
        login.click()

        # 2. Click 'username'
        username = selenium_driver.find_element(By.CSS_SELECTOR, "#username")
        username.click()

        # 3. Type '{project_parameters.UserID}' in 'username'
        username = selenium_driver.find_element(By.CSS_SELECTOR, "#username")
        username.send_keys(f"{project_parameters.UserID}")

        # 4. Click 'password'
        password = selenium_driver.find_element(By.CSS_SELECTOR, "#password")
        password.click()

        # 5. Type '{project_parameters.UserPWD}' in 'password'
        password = selenium_driver.find_element(By.CSS_SELECTOR, "#password")
        password.send_keys(f"{project_parameters.UserPWD}")

        # 6. Click 'login'
        login1 = selenium_driver.find_element(By.CSS_SELECTOR, "#kc-login")
        login1.click()

        # 7.1. Accept the terms if needed
        try:
            terms_checkbox = selenium_driver.find_element(
                By.XPATH, "//input[@id='tos']"
            )
            terms_checkbox.click()

            terms_accept = selenium_driver.find_element(
                By.XPATH, "//button[@type='submit']"
            )
            terms_accept.click()
        except Exception as e:
            print(e)

        # 7.2. Click '×' if needed
        try:
            _ = selenium_driver.find_element(By.XPATH, "//span[. = '×']")
            _.click()
        except Exception as e:
            print(e)

    def test_data(self):
        """Test datasets on federation."""
        selenium_driver = self.driver

        # 8. Click 'Dementia' /html/body/div[8]/main/div/div[1]/div/div[1]/div[1]/div[1]/div/div/a[1]
        dementia = selenium_driver.find_element(
            By.XPATH, "//div[@id='pathology-select']/div/button"
        )
        dementia.click()

        # 9. Click 'Mentalhealth'
        mentalhealth = selenium_driver.find_element(By.LINK_TEXT, "mentalhealth v7")
        mentalhealth.click()

        # 10. Click 'OK'
        ok = selenium_driver.find_element(By.XPATH, "//button[. = 'OK']")
        ok.click()

        # 11. Click 'Datasets'
        datasets = selenium_driver.find_element(By.CSS_SELECTOR, "#dropdown-basic")
        datasets.click()

        # 12. Click 'default-synth_mh_wk2'
        time.sleep(3)
        default_synth_mh_wk2 = selenium_driver.find_element(
            By.CSS_SELECTOR, "#default-synth_mh_wk2"
        )
        default_synth_mh_wk2.click()

        # 14. Click 'default-synth_mh_wk3'
        default_synth_mh_wk3 = selenium_driver.find_element(
            By.CSS_SELECTOR, "#default-synth_mh_wk3"
        )
        default_synth_mh_wk3.click()

        # 15. Click 'default-synth_mh_wk4'
        default_synth_mh_wk4 = selenium_driver.find_element(
            By.CSS_SELECTOR, "#default-synth_mh_wk4"
        )
        default_synth_mh_wk4.click()

        # 16. Click 'default-synth_mh_wk5'
        default_synth_mh_wk5 = selenium_driver.find_element(
            By.CSS_SELECTOR, "#default-synth_mh_wk5"
        )
        default_synth_mh_wk5.click()

        # 17. Click 'Left opercular part of the inferior f...'
        left_opercular_part_of_the_inferior_f_ = selenium_driver.find_element(
            By.XPATH,
            "//*[name()='circle'][. = 'Left opercular part of the inferior frontal gyrus\n']",
        )
        left_opercular_part_of_the_inferior_f_.click()

        # 18. Is the div containing the histogram of 'Left opercular part of the inferior f...' generated?
        histogram_of_leftopifgopercularpartof_ = selenium_driver.find_element(
            By.XPATH,
            "//div[contains(@id,'bar-graph-left-opercular-part-of-the-inferior-frontal-gyrus')]",
        )
        assert histogram_of_leftopifgopercularpartof_

        # 19. Click 'Right occipital fusiform gyrus'
        right_occipital_fusiform_gyrus = selenium_driver.find_element(
            By.XPATH, "//*[name()='circle'][. = 'Right occipital fusiform gyrus\n']"
        )
        right_occipital_fusiform_gyrus.click()

        # 20. Is the div containing the histogram of 'Right occipital fusiform gyrus' generated?
        histogram_of_rightofugoccipitalfusifo_ = selenium_driver.find_element(
            By.XPATH, "//div[contains(@id,'bar-graph-right-occipital-fusiform-gyrus')]"
        )
        assert histogram_of_rightofugoccipitalfusifo_

        # 21. Click 'Datasets'
        datasets = selenium_driver.find_element(By.CSS_SELECTOR, "#dropdown-basic")
        datasets.click()

        # 22. Click 'default-synth_mh_wk1'
        default_synth_mh_wk1 = selenium_driver.find_element(
            By.CSS_SELECTOR, "#default-synth_mh_wk1"
        )
        default_synth_mh_wk1.click()

        # 23. Click 'default-synth_mh_wk2'
        default_synth_mh_wk2 = selenium_driver.find_element(
            By.CSS_SELECTOR, "#default-synth_mh_wk2"
        )
        default_synth_mh_wk2.click()

        # 24. Click 'Sepa: afraid of being at home alone (...'
        sepa_colon_afraid_of_being_at_home_alone_ = selenium_driver.find_element(
            By.XPATH,
            "//*[name()='circle'][. = 'Sepa: afraid of being at home alone (youth)\nNightmares about separation from attachment figures in the past 4 weeks']",
        )
        sepa_colon_afraid_of_being_at_home_alone_.click()

        # 25. Is the div containing the histogram of 'Sepa: afraid of being at home alone (...' generated?
        histogram_of_sa3h = selenium_driver.find_element(
            By.XPATH,
            "//div[contains(@id,'bar-graph-sepa-afraid-of-being-at-home-alone-youth')]",
        )
        assert histogram_of_sa3h

        # 26. Click 'Right transverse temporal gyrus'
        right_transverse_temporal_gyrus = selenium_driver.find_element(
            By.XPATH, "//*[name()='circle'][. = 'Right transverse temporal gyrus\n']"
        )
        right_transverse_temporal_gyrus.click()

        # 27. Is the div containing the histogram of 'Right transverse temporal gyrus' generated?
        histogram_of_rightttgtransversetempor_ = selenium_driver.find_element(
            By.XPATH, "//div[contains(@id,'bar-graph-right-transverse-temporal-gyrus')]"
        )
        assert histogram_of_rightttgtransversetempor_

        # 28. Click 'Datasets'
        datasets = selenium_driver.find_element(By.CSS_SELECTOR, "#dropdown-basic")
        datasets.click()

        # 29. Click 'default-synth_mh_wk2'
        default_synth_mh_wk2 = selenium_driver.find_element(
            By.CSS_SELECTOR, "#default-synth_mh_wk2"
        )
        default_synth_mh_wk2.click()

        # 30. Click 'default-synth_mh_wk3'
        default_synth_mh_wk3 = selenium_driver.find_element(
            By.CSS_SELECTOR, "#default-synth_mh_wk3"
        )
        default_synth_mh_wk3.click()

        # 31. Click 'Right posterior cingulate gyrus1'
        right_posterior_cingulate_gyrus1 = selenium_driver.find_element(
            By.XPATH, "//*[name()='circle'][. = 'Right posterior cingulate gyrus\n']"
        )
        right_posterior_cingulate_gyrus1.click()

        # 32. Is the div containing the histogram of 'Right posterior cingulate gyrus1' generated?
        histogram_of_rightpcggposteriorcingul_ = selenium_driver.find_element(
            By.XPATH, "//div[contains(@id,'bar-graph-right-posterior-cingulate-gyrus')]"
        )
        assert histogram_of_rightpcggposteriorcingul_

        # 33. Click 'Sepa: any concerns about separations?...'
        sepa_colon_any_concerns_about_separations_question_mark_ = selenium_driver.find_element(
            By.XPATH,
            "//*[name()='circle'][. = 'Sepa: any concerns about separations? (youth)\nConcern about separation over the past 4 weeks']",
        )
        sepa_colon_any_concerns_about_separations_question_mark_.click()

        # 34. Is the div containing the histogram of 'Sepa: any concerns about separations?...' generated?
        histogram_of_sa2 = selenium_driver.find_element(
            By.XPATH,
            "//div[contains(@id,'bar-graph-sepa-any-concerns-about-separations-youth')]",
        )
        assert histogram_of_sa2

        # 35. Click 'Datasets'
        datasets = selenium_driver.find_element(By.CSS_SELECTOR, "#dropdown-basic")
        datasets.click()

        # 36. Click 'default-synth_mh_wk3'
        default_synth_mh_wk3 = selenium_driver.find_element(
            By.CSS_SELECTOR, "#default-synth_mh_wk3"
        )
        default_synth_mh_wk3.click()

        # 37. Click 'default-synth_mh_wk4'
        default_synth_mh_wk4 = selenium_driver.find_element(
            By.CSS_SELECTOR, "#default-synth_mh_wk4"
        )
        default_synth_mh_wk4.click()

        # 38. Click 'Right superior temporal gyrus'
        right_superior_temporal_gyrus = selenium_driver.find_element(
            By.XPATH, "//*[name()='circle'][. = 'Right superior temporal gyrus\n']"
        )
        right_superior_temporal_gyrus.click()

        # 39. Is the div containing the histogram of 'Right superior temporal gyrus' generated?
        histogram_of_rightstgsuperiortemporal_ = selenium_driver.find_element(
            By.XPATH, "//div[contains(@id,'bar-graph-right-superior-temporal-gyrus')]"
        )
        assert histogram_of_rightstgsuperiortemporal_

        # 40. Click 'Right inferior lateral ventricle1'
        right_inferior_lateral_ventricle1 = selenium_driver.find_element(
            By.XPATH, "//*[name()='circle'][. = 'Right inferior lateral ventricle\n']"
        )
        right_inferior_lateral_ventricle1.click()

        # 41. Is the div containing the histogram of 'Right inferior lateral ventricle1' generated?
        histogram_of_rightinflatvent = selenium_driver.find_element(
            By.XPATH,
            "//div[contains(@id,'bar-graph-right-inferior-lateral-ventricle')]",
        )
        assert histogram_of_rightinflatvent

        # 42. Click 'Datasets'
        datasets = selenium_driver.find_element(By.CSS_SELECTOR, "#dropdown-basic")
        datasets.click()

        # 43. Click 'default-synth_mh_wk4'
        default_synth_mh_wk4 = selenium_driver.find_element(
            By.CSS_SELECTOR, "#default-synth_mh_wk4"
        )
        default_synth_mh_wk4.click()

        # 44. Click 'default-synth_mh_wk5'
        default_synth_mh_wk5 = selenium_driver.find_element(
            By.CSS_SELECTOR, "#default-synth_mh_wk5"
        )
        default_synth_mh_wk5.click()

        # 45. Click 'Right entorhinal area'
        right_entorhinal_area = selenium_driver.find_element(
            By.XPATH, "//*[name()='circle'][. = 'Right entorhinal area\n']"
        )
        right_entorhinal_area.click()

        # 46. Is the div containing the histogram of 'Right entorhinal area' generated?
        histogram_of_rightententorhinalarea = selenium_driver.find_element(
            By.XPATH, "//div[contains(@id,'bar-graph-right-entorhinal-area')]"
        )
        assert histogram_of_rightententorhinalarea

        # 47. Click 'Left subcallosal area'
        left_subcallosal_area = selenium_driver.find_element(
            By.XPATH, "//*[name()='circle'][. = 'Left subcallosal area\n']"
        )
        left_subcallosal_area.click()

        # 48. Is the div containing the histogram of 'Left subcallosal area' generated?
        histogram_of_leftscasubcallosalarea = selenium_driver.find_element(
            By.XPATH, "//div[contains(@id,'bar-graph-left-subcallosal-area')]"
        )
        assert histogram_of_leftscasubcallosalarea
