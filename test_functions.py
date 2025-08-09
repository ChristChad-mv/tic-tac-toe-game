
import pytest
from functions import calculate_tip, is_prime, get_day_of_the_week, recommend_movie, celsius_to_fahrenheit, simple_interest, plan_weekly_groceries, generate_workout_plan, create_travel_itinerary, manage_task_list

def test_calculate_tip():
    assert calculate_tip(100, 10) == 10.0
    assert calculate_tip(50, 15) == 7.5
    assert calculate_tip(200, 20) == 40.0

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(17) == True
    assert is_prime(4) == False
    assert is_prime(1) == False

def test_get_day_of_the_week():
    assert get_day_of_the_week("2025-08-08") == "Friday"
    assert get_day_of_the_week("2024-12-25") == "Wednesday"
    assert get_day_of_the_week("2025-01-01") == "Wednesday"

def test_recommend_movie():
    assert recommend_movie("action") in ["Inception", "The Matrix", "Mad Max: Fury Road"]
    assert recommend_movie("comedy") in ["Superbad", "The Hangover", "Dumb and Dumber"]
    assert "Genre non reconnu" in recommend_movie("romance")

def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert celsius_to_fahrenheit(-40) == -40

def test_simple_interest():
    assert simple_interest(1000, 0.05, 5) == 250.0
    assert simple_interest(500, 0.1, 2) == 100.0
    assert simple_interest(2000, 0.02, 10) == 400.0

def test_plan_weekly_groceries():
    meal_plan = {"Pizza": 30, "Salad": 15, "Pasta": 20}
    budget = 70
    result = plan_weekly_groceries(budget, meal_plan)
    assert result["total_cost"] == 65
    assert "remaining_budget" in result
    
    budget = 50
    result = plan_weekly_groceries(budget, meal_plan)
    assert result["status"] == "budget_exceeded"

def test_generate_workout_plan():
    plan = generate_workout_plan(30, "cardio")
    assert "Warm-up" in plan
    assert "Workout" in plan
    assert "Cool-down" in plan
    assert len(plan["Workout"]) > 0
    
    plan = generate_workout_plan(10, "cardio")
    assert "error" in plan

def test_create_travel_itinerary():
    itinerary = create_travel_itinerary("paris", 3)
    assert "Jour 1" in itinerary
    assert "Jour 2" in itinerary
    assert "Jour 3" in itinerary
    
    itinerary = create_travel_itinerary("london", 2)
    assert "Explorer Activité touristique générale" in itinerary["Jour 1"]
    
    itinerary = create_travel_itinerary("paris", 0)
    assert "error" in itinerary

def test_manage_task_list():
    task_list = ["Task 1", "Task 2"]
    task_list = manage_task_list(task_list, "add", "Task 3")
    assert "Task 3" in task_list
    task_list = manage_task_list(task_list, "remove", "Task 1")
    assert "Task 1" not in task_list
    task_list = manage_task_list(task_list, "show")
    assert len(task_list) == 2
