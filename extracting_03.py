import re

# TODO:
#  1. Get Twitter/IG/main account
#  2. 3rd party social media tool
#  3. Define a email sender
#  4. Manage related conversation with influencers
#  4. Chatbot for FAQ

# Extracting email
def extract_email(text):
    # Regular expression pattern to match email addresses
    email_pattern = r"[a-zA-Z0-9._%!#$%^&*()\+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    # Find all matches in the text
    emails = re.findall(email_pattern, text)
    if not emails:
        return '暂无联系方式'
    # try:
    #     return ',\n'.join(emails)
    # except:
    return ',\n'.join(emails)

def extract_websites(text):
    # Remove email-like patterns from the text
    email_pattern = r"[a-zA-Z0-9._%!#$%^&*()\+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    text_without_emails = re.sub(email_pattern, '', text)
    # Further refined regex pattern to try and capture standalone domains without "http://" or "https://" prefix
    url_pattern = r'(?:(?<=\s)|(?<=^)|(?<=\W))(http(s)?://[\w\-@./]+|(?<![a-zA-Z0-9@])[\w\-]+(?:\.[a-zA-Z]{2,4})(?:(?:\.[a-zA-Z]{2,4})?)(?![a-zA-Z0-9@\.])[\w\-@./]*)'
    websites = re.findall(url_pattern, text_without_emails)
    if not websites:
        return '暂无相关网页'
    # Post-process to remove trailing periods from domain names or URLs
    return ',\n'.join([site for tuple_item in websites for site in tuple_item if site])


# Extract phone number -US Phone number
def extract_phone_numbers(text):
    # Regular expression pattern to match phone numbers
    phone_pattern = r'(\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4})'
    # Find all matches in the text
    phone_numbers = re.findall(phone_pattern, text)
    return phone_numbers


# Extracting and combining emails from the entire DataFrame
def email_from_df(df):
    all_emails = []
    for _, row in df.iterrows():
        cell = row.iloc[4]
        email = extract_email(cell)
        if email != '暂无联系方式':
            all_emails.append(email)
    return ', '.join(all_emails)
