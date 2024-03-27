import random
import re

class SupportBot:
    negative_res = ("no", "nope", "nay", "not a chance", "sorry")
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "farewell")

    def __init__(self):
        self.support_responses = {
            'ask_about_products': r'.*\s*product.*',
            'technical_support': r'.*technical.*support.*',
            'about_returns': r'.*\s*returnpolicy.*',
            'general_query': r'.*show.*help.*'
        }

    def greet(self):
        self.name = input("Hello! Welcome to customer support. What's your name?\n")
        will_help = input(f"Hi {self.name}, how can I assist you today?\n")
        if will_help in self.negative_res:
            print("Alright, have a great day!")
            return
        self.chat()

    def make_exit(self, reply):
        for command in self.exit_commands:
            if command in reply:
                print("Thanks for reaching out. Have a great day!")
                return True
        return False

    def chat(self):
        reply = input("Please tell me your query: ").lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply))

    def match_reply(self, reply):
        for intent, regex_pattern in self.support_responses.items():
            found_match = re.search(regex_pattern, reply)
            if found_match and intent == 'ask_about_products':
                return self.ask_about_product()
            elif found_match and intent == 'technical_support':
                return self.technical_support()
            elif found_match and intent == 'about_returns':
                return self.about_returns()
            elif found_match and intent == 'general_query':
                return self.general_query()
        return self.no_match_intent()

    def ask_about_product(self):
        responses = ("Our groceries are fresh and have healthy reviews.\n",
                     "You can find all product details on our website.\n")
        return random.choice(responses)

    def technical_support(self):
        responses = ("You can visit our technical support page for assistance.\n",
                     "You can call our technical support team for immediate assistance.\n")
        return random.choice(responses)

    def about_returns(self):
        responses = ("Our product has a 7-day return policy.\n",
                     "Return will not be initiated if the product was not in original condition.\n")
        return random.choice(responses)

    def general_query(self):
        responses = ("How can I help you further?\n",
                     "Is there anything else you want to know?\n")
        return random.choice(responses)

    def no_match_intent(self):
        responses = ("I'm sorry, I didn't understand that. Can you please rephrase?\n",
                     "My apologies, can you provide more detail?\n")
        return random.choice(responses)

bot = SupportBot()
bot.greet()
