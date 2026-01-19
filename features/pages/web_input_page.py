from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage


class WebInputPage(BasePage):


    # -------- Locators --------
    # -------- Input Locators --------
    link_web_inputs_page = (By.LINK_TEXT, "Web inputs")
    input_number = (By.ID, "input-number")
    input_text = (By.ID, "input-text")
    input_password = (By.ID, "input-password")
    input_date = (By.ID, "input-date")
    button_display_inputs = (By.ID, "btn-display-inputs")
    button_clear_inputs = (By.ID, "btn-clear-inputs")

    # -------- Output Locators --------
    output_number = (By.ID, "output-number")
    output_text = (By.ID, "output-text")
    output_password = (By.ID, "output-password")
    output_date = (By.ID, "output-date")

    # -------- Page Actions --------
    def open(self):
        self.click(self.link_web_inputs_page)
    
    def enter_number(self, number):
        self.type(self.input_number, number)
    
    def enter_text(self, text):
        self.type(self.input_text, text)
    
    def enter_password(self, password):
        self.type(self.input_password, password)
    
    def enter_date(self, date):
        self.type(self.input_date, date)
    
    def click_display_inputs(self):
        self.click(self.button_display_inputs)
    
    def click_clear_inputs(self):
        self.click(self.button_clear_inputs)
    
    # --- Getters (For Verifying Output) ---
    def get_input_number(self):
        return self.get_text(self.output_number)
    
    def get_input_text(self):
        return self.get_text(self.output_text)
    
    def get_input_password(self):
        return self.get_text(self.output_password)
    
    def get_input_date(self):
        return self.get_text(self.output_date)
    
    # --- Getters (For Verifying Clear Button works) ---
    def get_number_value(self):
        return self.get_attribute(self.input_number, "value")
    
    def get_text_value(self):
        return self.get_attribute(self.input_text, "value")
    
    def get_password_value(self):
        return self.get_attribute(self.input_password, "value")
    
    def get_date_value(self):
        return self.get_attribute(self.input_date, "value")
