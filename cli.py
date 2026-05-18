#cli.py
class UI:
    def show_ui(self):
        print("CALCULATOR")
        print("1. ADD")
        print("2. SUBSTRACT")
        print("3. MULTIPLY")
        print("4. DIVIDE")
        print("5. EXIT")
    
    def decorate(self,num:int):
        print("="*50)
        print("Answer",num)
        print("="*50)
    
    
