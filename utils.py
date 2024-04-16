import google.generativeai as genai
with open(r'C:\Users\dsai9\Projects\Gen AI apps\GEMINI_API_KEY.txt', 'r') as f:
    api_key = f.read().strip()

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')

sys_instruction='''
        You are a code reviewer. Your job is to review code and provide feedback. You must provide a ordered list of bugs present within the code
        then the correct version of the code. As you only provide correct responses, I want to crosscheck your reponses five times. 
        
        
        The response should be in following format
        
        heading 1: Code Review
        
        heading2: Bug Report
        List of bugs
        
        heading2: 
        Refactored Code
'''
def getReview(code):
    prompt=sys_instruction+'Instruction: Review the following code'+code
    
    response=model.generate_content(prompt)
    
    return response
    