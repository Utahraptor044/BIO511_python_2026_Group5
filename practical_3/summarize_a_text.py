


def summarize_text(s):
    summary = {'digits': 0, 'letters': 0, 'other': 0 }

    for l in s:
        if l.isdigit():
            summary['digits'] += 1
        elif l.isalpha():
            summary['letters'] += 1
        else:
            summary['other'] += 1
    return summary


text = 'Inside the function, create a local variable named summary that holds a dictionary with exactly these keys: "digits", "letters" and "other". Each key should start at 0.'
text_summarized = summarize_text(text)
print(text_summarized)
"""
diff = len(text) - text_summarized['digits'] - text_summarized['letters']
print(f'Length of text minus (the digits and letters) {diff}')
"""
