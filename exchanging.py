from fpdf import FPDF

# Create instance of FPDF class
pdf = FPDF()

# Add a page
pdf.add_page()

# Set title and font
pdf.set_font("Arial", 'B', 16)
pdf.cell(200, 10, txt="Daily Routine with Gym, Communication Skills, Hobbies, Skin Care, and Girlfriend Time", ln=True, align='C')

# Add space
pdf.ln(10)

# Daily Routine with Gym, Communication Skills, Hobbies, Skin Care, and Girlfriend Time
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="1. Daily Routine", ln=True)
pdf.ln(5)

# Using simpler quotes and apostrophes in the text
text = """
- **Morning Routine** (Before College):
    - 6:00 AM: Wake up, freshen up, and hydrate (drink water).
    - 6:15 AM: Morning stretching or yoga (15-20 minutes) to wake up the body.
    - 6:45 AM: Breakfast with a focus on protein and healthy fats.
    - 7:15 AM: Personal hygiene and skin care (cleansing, moisturizing).
    - 7:30 AM: Spend 20 minutes on communication skills (speaking exercises, watching TED Talks, etc.).
    - 8:00 AM: Review goals and set the tone for the day.
    - 8:15 AM: Leave for college.

- **College Routine** (9:30 AM - 4:30 PM):
    - Focus on studies and assignments.
    - Make time for networking with peers (communication skills practice).
    - Lunch break: Eat a balanced meal with protein and vegetables.

- **Post-College Routine** (5:00 PM - 7:00 PM):
    - 5:00 PM: Arrive home, freshen up, and have a quick snack (e.g., protein shake or fruits).
    - 5:30 PM: Gym workout (Chest & Triceps, Back & Biceps, etc.).
    - 7:00 PM: Post-workout meal (focus on protein and carbs for recovery).

- **Evening Routine** (7:30 PM - 9:30 PM):
    - 7:30 PM: Communication practice (write daily journal, engage in a conversation, improve your vocabulary).
    - 8:00 PM: Spend quality time with your girlfriend (watch a movie, have a conversation, go for a walk).
    - 9:00 PM: Skin care (apply moisturizer, sunscreen, etc.).
    - 9:30 PM: Prepare for the next day (set goals, pack your bag).

- **Night Routine** (10:00 PM - 10:30 PM):
    - 10:00 PM: Relax and unwind (light reading, listening to music, meditation).
    - 10:30 PM: Sleep and rest.

- **Extra Time for Hobbies**:
    - Find 30 minutes each day for a hobby (e.g., reading, painting, coding, or music).
    - Dedicate weekends or free days to a deeper dive into your hobbies or skills.
"""

pdf.multi_cell(0, 10, text)

# Add space
pdf.ln(5)

# Explanation of the Routine
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Explanation of the Daily Routine:", ln=True)
pdf.ln(5)

# Using simpler quotes and apostrophes in the explanation text
explanation_text = """
1. **Morning Routine**:
    - Hydrate and start the day with stretching or yoga to activate your body.
    - Focus on nutrition with a healthy breakfast to fuel the day.
    - Spend time on communication skills through exercises and learning from TED Talks or online resources.
    - Personal hygiene and skin care set the tone for self-care and confidence.

2. **College Routine**:
    - Focus on your studies and networking at college.
    - Use lunchtime to have a balanced meal and chat with peers to practice social skills.

3. **Post-College Routine**:
    - After college, refresh yourself with a snack and prepare for your gym workout.
    - Gym workout targets building strength and improving your physique. Focus on specific muscle groups each day (e.g., Chest & Triceps, Back & Biceps).

4. **Evening Routine**:
    - Communication practice helps in enhancing language and speaking fluency.
    - Spend quality time with your girlfriend to maintain a balanced social life.
    - Skin care enhances your physical appearance and boosts confidence.

5. **Night Routine**:
    - Use relaxation techniques to wind down and prepare for a restful night.
    - Ensure adequate sleep to recharge for the next day.

6. **Extra Time for Hobbies**:
    - Dedicate time each day to hobbies to improve creativity and relieve stress. Weekends allow deeper focus on your interests or passions.
"""

pdf.multi_cell(0, 10, explanation_text)

# Save the PDF to a file
file_path = "Daily_Routine_with_Gym_Communication_Hobbies_Skin_Care_and_Girlfriend_Time.pdf"
pdf.output(file_path)

file_path  # Return the file path for download.
