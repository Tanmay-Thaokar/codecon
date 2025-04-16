from utils.extractor import extract_text_from_pdf
from utils.summarizer import summarize_text_openai
from utils.explain import  explain_text_plain_english
from utils.clause_detector import detect_clauses

PDF_PATH = "test doc.pdf"


text = extract_text_from_pdf(PDF_PATH)
print("✅ Text Extracted")


summary = summarize_text_openai(text)
print("\n📝 Summary:\n", summary)


clauses = detect_clauses(text)
print("\n🔍 Detected Clauses:")
for clause, matches in clauses.items():
    print(f"{clause}: {matches[:2]}")  # Show sample match


print("\n💡 Simplified Explanation:")
explanation = explain_text_plain_english(text)
print(explanation)




# calling supabase for supa-base 
from supabase import create_client
import time

url = "https://haxbnnottbryxkrnekir.supabase.co/"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhheGJubm90dGJyeXhrcm5la2lyIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc0NDc4NDE4NSwiZXhwIjoyMDYwMzYwMTg1fQ.aJPOPAIeUMizyLBjDZ36gzLSZlSiCPBE9FKEWWDeOJ0"  # use service key, not anon key

supabase = create_client(url, key)

def get_new_files():
    # Fetch latest file metadata from Supabase table (if you're tracking them)
    response = supabase.table('documents').select('*').order('created_at', desc=True).limit(1).execute()
    return response.data

def analyze_and_update(file_url, record_id):
    # Analyze the file (download it first)
    import requests
    content = requests.get(file_url).content

    result = run_your_ai_model(content)  # 🔍 custom analyzer function

    # Update result back to the Supabase table
    supabase.table('documents').update({"analysis_result": result}).eq("id", record_id).execute()

# Poll loop (or trigger this with a webhook/cron)
while True:
    files = get_new_files()
    for f in files:
        if not f["analysis_result"]:
            analyze_and_update(f["public_url"], f["id"])
    time.sleep(10)  # check every 10s
