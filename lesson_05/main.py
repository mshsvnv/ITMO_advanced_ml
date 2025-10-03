# Наивный баесовский классификатор
import numpy as np

letters = [19, 12]
words = [59, 55]

d = {'Money': [1, 2],
     'Purchase': [3, 0],
     'Membership': [0, 3],
     'Free': [3, 0],
     'Refund': [7, 4],
     'Cash': [11, 5],
     'Bonus': [2, 4],
     'Offer': [3, 9],
     'Online': [0, 11],
     'Coupon': [29, 17]}

spam, not_spam = 0, 1

P_spam = letters[spam] / sum(letters)
P_not_spam = letters[not_spam] / sum(letters)

v = len(d)

email_words = ["Coupon", "Refund", "Gift", "Unlimited", "Offer", "Purchase", "Membership"]

r = 0
for word in email_words:
    r += word not in d.keys()

def F(P, cls):
    F = np.log(P)
    for word in email_words:
        
        if word in d.keys():
            F += np.log((1 + d[word][cls]) / (v + r + words[cls]))
        else:
            F += np.log(1 / (v + r + words[cls]))
    return F

F_spam = F(P_spam, spam)
F_not_spam = F(P_not_spam, not_spam)

F = np.exp(F_spam) + np.exp(F_not_spam)
P_spam_given_email = np.exp(F_spam) / F

print(f'Вероятность того, что письмо является спамом: {P_spam:.3f}')
print(f"F(\"спам\"): {F_spam:.3f}")
print(f"F(\"не спам\"): {F_not_spam:.3f}")
print(f'P(спам | письмо): {P_spam_given_email:.3f}')