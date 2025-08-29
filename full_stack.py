from fastapi import FastAPI
from pydantic import BaseModel
import re

app = FastAPI()

class DataModel(BaseModel):
    data: list

def alternating_caps_reverse(s):
    result, toggle = "", True
    for ch in s[::-1]:
        result += ch.upper() if toggle else ch.lower()
        toggle = not toggle
    return result

@app.post("/bfhl")
async def process_data(req: DataModel):
    try:
        data = req.data
        even_numbers, odd_numbers, alphabets, special_chars = [], [], [], []
        total_sum, alpha_string = 0, ""

        for item in data:
            if re.fullmatch(r"\d+", item):
                num = int(item)
                total_sum += num
                (even_numbers if num % 2 == 0 else odd_numbers).append(item)
            elif item.isalpha():
                alphabets.append(item.upper())
                alpha_string += item
            else:
                special_chars.append(item)

        return {
            "is_success": True,
            "user_id": "KURARITHEESH123",
            "email": "ritheeshk2003@gmail.com",
            "roll_number": "22BCE0561",
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_chars,
            "sum": str(total_sum),
            "concat_string": alternating_caps_reverse(alpha_string)
        }
    except Exception as e:
        return {"is_success": False, "message": str(e)}

