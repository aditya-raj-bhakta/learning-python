from fpdf import FPDF

# Create instance of FPDF class
pdf = FPDF()

# Add a page
pdf.add_page()

# Set title and font
pdf.set_font("Arial", 'B', 16)
pdf.cell(200, 10, txt="Daily Routine with Girlfriend Time", ln=True, align='C')

# Add space
pdf.ln(10)

# Regular Routine with Girlfriend Time
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="1. Regular Routine (With Time for Your Girlfriend)", ln=True)
pdf.ln(5)

pdf.multi_cell(0, 10, """
- **6:30 AM - Wake Up & Freshen Up**: Healthy breakfast and hydrate.
- **7:00 AM - 8:00 AM - DSA Study (1 hour)**: Focus on study and problem-solving.
- **8:00 AM - 8:30 AM - Skin Care Routine (30 minutes)**: Cleanse, tone, and moisturize for healthier skin.
- **9:30 AM - 4:30 PM - College**: Attend college classes, take breaks if possible.
- **5:00 PM - 6:00 PM - Free Time with Girlfriend (1 hour)**: Catch up with her, relax, chat, or do something fun together.
- **6:00 PM - 7:00 PM - Gym (1 hour)**: Strength training or cardio.
- **7:00 PM - 7:30 PM - Skin Care (30 minutes)**: Night-time skincare, including moisturizing.
- **7:30 PM - 8:00 PM - Dinner**: Healthy meal for recovery.
- **8:00 PM - 8:30 PM - Communication Skills Practice (30 minutes)**: Read books or practice conversational skills.
- **8:30 PM - 9:00 PM - Hobby Time (30 minutes)**: Spend time on your hobby (e.g., drawing, playing an instrument).
- **9:00 PM - 10:00 PM - Free Time with Girlfriend (1 hour)**: Relax and unwind.
- **10:00 PM - Sleep**: Rest for the next day.
""")

# Add space
pdf.ln(5)

# Holiday Routine with Girlfriend Time
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="2. Holiday Routine (With Time for Your Girlfriend)", ln=True)
pdf.ln(5)

pdf.multi_cell(0, 10, """
- **8:00 AM - Wake Up & Freshen Up**: Start your day with a healthy breakfast.
- **8:30 AM - 9:00 AM - Skin Care (30 minutes)**: Cleanse and hydrate.
- **9:00 AM - 10:00 AM - DSA Study (1 hour)**: Study a specific topic.
- **10:00 AM - 11:00 AM - Hobby Time (1 hour)**: Engage in a hobby like painting or learning a new skill.
- **11:00 AM - 12:00 PM - Gym (1 hour)**: Full-body workout or targeted muscles.
- **12:00 PM - 1:00 PM - Lunch**: Balanced meal to fuel you.
- **1:00 PM - 3:00 PM - DSA Study (2 hours)**: Continue studying or solving problems.
- **3:00 PM - 4:00 PM - Free Time with Girlfriend (1 hour)**: Quality time with her.
- **4:00 PM - 5:00 PM - Communication Skills Practice (1 hour)**: Practice by talking, listening to podcasts, or engaging in discussions.
- **5:00 PM - 6:30 PM - Optional Gym or Light Cardio (1.5 hours)**: Optional light exercise.
- **6:30 PM - 7:00 PM - Dinner**: Refuel with a healthy meal.
- **7:00 PM - 8:00 PM - DSA Study (1 hour)**: Focus on solving problems.
- **8:00 PM - 9:00 PM - Free Time with Girlfriend (1 hour)**: Relax or enjoy an activity together.
- **9:00 PM - 10:00 PM - Skin Care (30 minutes)**: Cleanse and moisturize your skin.
- **10:00 PM - Sleep**: Rest for the next day.
""")

# Add space
pdf.ln(5)

# Exam Day Routine with Girlfriend Time
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="3. Exam Day Routine (With Girlfriend Time)", ln=True)
pdf.ln(5)

pdf.multi_cell(0, 10, """
- **6:30 AM - Wake Up & Freshen Up**: Healthy breakfast and hydrate.
- **7:00 AM - 8:00 AM - DSA Review (1 hour)**: Quick revision of key concepts.
- **8:00 AM - 9:00 AM - Light Exercise (Walk or Yoga)**: Light exercise to reduce stress.
- **9:00 AM - 9:30 AM - Breakfast & Prepare for Exam**: Eat a nutritious breakfast and get ready.
- **9:30 AM - 4:30 PM - Exam & College Work**: Focus on your exams. Take short breaks if allowed.
- **5:00 PM - 6:00 PM - Relaxation & Snack**: Hydrate and have a light snack after the exam.
- **6:00 PM - 7:00 PM - Skin Care (30 minutes)**: Cleanse and moisturize your skin.
- **7:00 PM - 7:30 PM - Light Gym / Cardio**: Cardio or a light gym session.
- **7:30 PM - 8:00 PM - Dinner**: Refuel with a healthy meal.
- **8:00 PM - 9:00 PM - Communication Skills Practice (1 hour)**: Practice speaking and listening exercises.
- **9:00 PM - 10:00 PM - Spend Time with Girlfriend (1 hour)**: Relax and bond with your girlfriend.
- **10:00 PM - Sleep**: Rest well for the next day.
""")

# Add space
pdf.ln(5)

# Explanation for Regular Routine
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Explanation of the Regular Routine:", ln=True)
pdf.ln(5)

pdf.multi_cell(0, 10, """
1. **Morning Routine**: Wake up refreshed with a healthy breakfast and a productive study session. 
   Start the day with focus on DSA (Data Structures and Algorithms), which helps improve your problem-solving skills.

2. **College Time**: College classes are your primary work hours. During breaks, take a walk or chat with friends.

3. **Post-College and Evening Routine**: After college, dedicate time for fitness (strength training or cardio).
   Having an evening workout helps you relieve stress and maintain your physical health.
   Dinner should be nutritious to support your body’s recovery after the workout.

4. **Communication Skills Practice**: This time is to help you improve your speaking and listening skills. You can read, engage in discussions, or watch videos to practice articulation and confidence.

5. **Hobby Time**: Whether it’s playing an instrument, drawing, or learning a new skill, this time nurtures your passions outside of studies.

6. **Skin Care**: A 30-minute skincare routine in the morning and evening helps you maintain healthy skin, hydrate, and refresh yourself.

7. **Free Time with Girlfriend**: Spending time with your girlfriend allows for emotional connection and relaxation after a busy day. 
   End the day by unwinding and getting adequate rest for the following day.
""")

# Add space
pdf.ln(5)

# Explanation for Holiday Routine
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Explanation of the Holiday Routine:", ln=True)
pdf.ln(5)

pdf.multi_cell(0, 10, """
1. **Morning Routine**: Wake up early, have a good breakfast, and start your day with focused study time (DSA).

2. **Gym Session**: Morning gym sessions (1.5 - 2 hours) will help you maintain physical health and energy throughout the day.

3. **Hobby Time**: Use your holiday to engage in a hobby or learn a new skill. It gives you a creative outlet and helps relieve stress.

4. **Afternoon Routine**: Continue with a well-balanced lunch and additional DSA study time to dive deeper into your learning. 
   Post-study, use your free time to bond with your girlfriend (taking a walk or enjoying an activity together).

5. **Review & Optional Light Cardio**: Review what you studied and consider a second light gym session for active recovery. 
   Evening study helps reinforce your learning while giving you time for relaxation.

6. **Girlfriend Time**: Ending your day with quality time ensures a balanced approach to personal and academic life.
""")

# Add space
pdf.ln(5)

# Explanation for Exam Day Routine
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Explanation of the Exam Day Routine:", ln=True)
pdf.ln(5)

pdf.multi_cell(0, 10, """
1. **Morning Routine**: Start with a light breakfast and some morning revision (DSA), which keeps your mind sharp for the exam.

2. **Light Exercise**: Light stretching or walking helps relieve exam anxiety and helps maintain your energy levels.

3. **Exam & College Work**: Focus on your exam during this time. Keep your study breaks short and stay hydrated.

4. **Post-Exam Routine**: After your exam, relax and refuel your body with healthy snacks or light food. A light gym session (or cardio) helps keep you energized.

5. **Communication Skills Practice**: Practice speaking skills or listen to a podcast to continue honing your communication even on exam days.

6. **Wind Down & Girlfriend Time**: After a long exam day, spend some relaxing time with your girlfriend to reduce stress and bond.
   Ensure a good night’s sleep for optimal focus during the next day’s exam or study session.
""")

# Save the PDF to a file
file_path = "Updated_Daily_Routines_With_Girlfriend_Time_And_Explanations.pdf"
pdf.output(file_path)

file_path  # Return the file path for download.
