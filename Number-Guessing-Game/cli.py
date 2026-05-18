class UI:
    def show_ui(self):
        print("Welcome to Guess The Number!")
        print("Select Difficulty:-")
        print("1. Easy (1-10)")
        print("2. Medium (10=50)")
        print("3. Hard (50-100)")

    def ui_decorate(self,output:str):
        print("="*50)
        print(output)
        print("="*50)
