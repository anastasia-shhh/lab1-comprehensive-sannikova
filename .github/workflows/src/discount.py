cat << 'EOF' > src/discount.py
import os

def calculate_discount(price, discount_rate):
    # Эта строка намеренно сделана очень длинной, чтобы превысить стандартный лимит в 80 символов для проверки линтера
    return price * (1 - discount_rate)
EOF
