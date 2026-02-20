def ml_predict_performance():
    # Fetch all data
    cursor.execute("SELECT total, percentage FROM students")
    data = cursor.fetchall()

    if len(data) < 2:
        print("❌ Not enough data to train ML model (Need at least 2 students)")
        return

    # Prepare dataset
    totals = []
    percentages = []

    for row in data:
        totals.append(row[0])
        percentages.append(row[1])

    X = np.array(totals).reshape(-1, 1)
    y = np.array(percentages)

    # Train Model
    model = LinearRegression()
    model.fit(X, y)

    print("✅ ML Model Trained Successfully")

    # Take new input
    new_total = int(input("Enter total marks to predict future percentage: "))
    predicted_percentage = model.predict([[new_total]])

    print(f"🧠 Predicted Future Percentage: {predicted_percentage[0]:.2f}")

    # Grade Prediction
    grade = calculate_grade(predicted_percentage[0])
    print(f"📊 Predicted Grade: {grade}")
