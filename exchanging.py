from fpdf import FPDF

# Create instance of FPDF class
pdf = FPDF()

# Add a page
pdf.add_page()

# Set title and font
pdf.set_font("Arial", 'B', 16)
pdf.cell(200, 10, txt="Comprehensive Routine: Gym, Daily Schedule, and Diet Plan", ln=True, align='C')

# Add space
pdf.ln(10)

# Gym Routine
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="1. Gym Routine (Weekly Schedule)", ln=True)
pdf.ln(5)

# Add Gym Routine details with exercises
gym_routine_text = """
**Monday (Chest & Triceps):**
- Chest Press (4 sets, 12 reps)
- Push-Ups (4 sets, 15-20 reps)
- Tricep Dips (4 sets, 12 reps)
- Cable Tricep Pushdowns (4 sets, 12 reps)
- Dumbbell Chest Flyes (4 sets, 12 reps)

**Tuesday (Back & Biceps):**
- Deadlifts (4 sets, 10-12 reps)
- Bent Over Rows (4 sets, 12 reps)
- Lat Pulldown (4 sets, 12 reps)
- Barbell Curl (4 sets, 12 reps)
- Hammer Curl (4 sets, 12 reps)

**Wednesday (Leg Day):**
- Squats (4 sets, 12 reps)
- Lunges (4 sets, 12 reps)
- Leg Press (4 sets, 12 reps)
- Calf Raises (4 sets, 20 reps)

**Thursday (Shoulders & Abs):**
- Shoulder Press (4 sets, 12 reps)
- Lateral Raise (4 sets, 12 reps)
- Front Raise (4 sets, 12 reps)
- Plank (3 sets, 30 seconds)
- Russian Twists (4 sets, 20 reps)

**Friday (Full Body):**
- Deadlift (4 sets, 10 reps)
- Bench Press (4 sets, 10 reps)
- Pull-Ups (3 sets, as many as possible)
- Squats (3 sets, 12 reps)

**Saturday (Active Recovery):**
- Light cardio (30 minutes)
- Stretching or Yoga (20 minutes)
"""

pdf.multi_cell(0, 10, gym_routine_text)

# Add space
pdf.ln(5)

# Daily Routine
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="2. Daily Routine with Gym, Communication Skills, Hobbies, Skin Care, and Girlfriend Time", ln=True)
pdf.ln(5)

# Add Daily Routine details
daily_routine_text = """
**Early Morning (6:00 AM - 6:30 AM):**
- Warm water with lemon + Soaked almonds and walnuts
- Hydrate and set goals for the day

**Breakfast (6:30 AM - 7:00 AM):**
- Oats Upma with boiled egg or Moong Dal Chilla with buttermilk

**Pre-Workout Snack (4:30 PM - 5:00 PM):**
- Banana with peanut butter or Greek Yogurt with honey and flax seeds

**Post-Workout (7:00 PM):**
- Protein Shake, boiled eggs (2), fruit

**Dinner (8:00 PM - 9:00 PM):**
- Grilled Chicken with steamed veggies and quinoa or Palak Tofu Curry with chapati

**Bedtime Snack (9:30 PM):**
- Cottage cheese (Paneer) or Warm Milk with turmeric

**Free Time for Girlfriend (9:00 PM - 9:30 PM):**
- Quality time together (movies, walk, conversations)

**Skin Care (9:00 PM - 9:30 PM):**
- Moisturize, apply sunscreen
"""

pdf.multi_cell(0, 10, daily_routine_text)

# Add space
pdf.ln(5)

# Diet Plan with Time Table
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="3. Diet Plan with Timing and Nutritional Breakdown", ln=True)
pdf.ln(5)

# Add Diet Plan with meal timings and nutritional info
diet_plan_text = """
**Early Morning (6:00 AM - 6:30 AM):**
- Warm Water with Lemon + Soaked Almonds and Walnuts
  - Nutritional Benefits: Helps digestion, metabolism boost, healthy fats

**Breakfast (6:30 AM - 7:00 AM):**
- Option 1: Oats Upma with boiled egg
- Option 2: Moong Dal Chilla with Buttermilk
  - Nutritional Benefits: High protein, fiber, good carbs

**Pre-Workout Snack (4:30 PM - 5:00 PM):**
- Banana with Peanut Butter or Greek Yogurt with Honey and Flaxseeds
  - Nutritional Benefits: Quick energy and healthy fats

**Post-Workout (7:00 PM):**
- Protein Shake + Boiled Eggs (2) or Paneer + Fruit
  - Nutritional Benefits: Muscle recovery, protein, vitamins

**Dinner (8:00 PM - 9:00 PM):**
- Option 1: Grilled Chicken + Steamed Veggies + Brown Rice
- Option 2: Palak Tofu Curry + Chapati
- Option 3: Chana Masala + Brown Rice
  - Nutritional Benefits: Protein-packed meals, complex carbs for recovery

**Bedtime Snack (9:30 PM - 10:00 PM):**
- Cottage Cheese (Paneer) or Warm Milk with Turmeric
  - Nutritional Benefits: Casein protein, muscle recovery

**Hydration:**
- Drink 3-4 liters of water daily to stay hydrated and support muscle function.
"""

pdf.multi_cell(0, 10, diet_plan_text)

# Add space
pdf.ln(5)

# Add a table for daily meal nutritional breakdown
pdf.set_font("Arial", 'B', 12)
pdf.cell(50, 10, "Meal", 1, 0, 'C')
pdf.cell(50, 10, "Calories", 1, 0, 'C')
pdf.cell(50, 10, "Protein", 1, 0, 'C')
pdf.cell(50, 10, "Carbs", 1, 0, 'C')
pdf.cell(50, 10, "Fats", 1, 1, 'C')

# Table data
meal_data = [
    ("Early Morning", "100", "3g", "10g", "7g"),
    ("Breakfast", "400", "20g", "50g", "10g"),
    ("Pre-Workout", "200", "6g", "30g", "8g"),
    ("Post-Workout", "350", "25g", "40g", "5g"),
    ("Dinner", "500", "35g", "40g", "20g"),
    ("Bedtime Snack", "200", "15g", "15g", "10g")
]

# Populate table
pdf.set_font("Arial", size=10)
for meal in meal_data:
    pdf.cell(50, 10, meal[0], 1, 0, 'C')
    pdf.cell(50, 10, meal[1], 1, 0, 'C')
    pdf.cell(50, 10, meal[2], 1, 0, 'C')
    pdf.cell(50, 10, meal[3], 1, 0, 'C')
    pdf.cell(50, 10, meal[4], 1, 1, 'C')

# Save the PDF to a file
file_path = "Comprehensive_Routine_Gym_Diet_Plan.pdf"
pdf.output(file_path)

file_path  # Return the file path for download.
