# real_life_agent.py

import random
from datetime import datetime, timedelta

# --- Fonctions Courtes ---
# Elles résolvent une petite tâche simple et directe.

def calculate_tip(bill_amount: float, tip_percentage: float = 15.0) -> float:
    """Calcule le pourboire pour une note de restaurant."""
    return bill_amount * (tip_percentage / 100)

def is_prime(n: int) -> bool:
    """Vérifie si un nombre est premier."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_day_of_the_week(date_str: str) -> str:
    """Retourne le jour de la semaine pour une date donnée (format 'YYYY-MM-DD')."""
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    return date_obj.strftime('%A')

def recommend_movie(genre: str) -> str:
    """Recommande un film aléatoire en fonction d'un genre."""
    movies = {
        "action": ["Inception", "The Matrix", "Mad Max: Fury Road"],
        "comedy": ["Superbad", "The Hangover", "Dumb and Dumber"],
        "sci-fi": ["Dune", "Blade Runner 2049", "Interstellar"],
        "horror": ["Hereditary", "The Exorcist", "Get Out"]
    }
    return random.choice(movies.get(genre.lower(), ["Genre non reconnu. Essayez action, comedy, sci-fi ou horror."]))

def celsius_to_fahrenheit(celsius: float) -> float:
    """Convertit une température de Celsius en Fahrenheit."""
    return (celsius * 9/5) + 32

def simple_interest(principal: float, rate: float, years: int) -> float:
    """Calcule l'intérêt simple sur une somme d'argent."""
    return principal * rate * years

# --- Fonctions Plus Larges ---
# Ces fonctions sont plus complexes et combinent plusieurs étapes logiques.

def plan_weekly_groceries(weekly_budget: float, meal_plan: dict) -> dict:
    """
    Planifie une liste de courses en fonction d'un budget et d'un plan de repas.
    
    Args:
        weekly_budget (float): Le budget total pour les courses de la semaine.
        meal_plan (dict): Un dictionnaire où les clés sont des plats et les valeurs sont leurs coûts estimés.
        
    Returns:
        dict: Un plan d'achat et le coût total, ou une alerte si le budget est dépassé.
    """
    shopping_list = {}
    total_cost = 0.0

    print("Création du plan de courses...")
    for meal, cost in meal_plan.items():
        if total_cost + cost <= weekly_budget:
            shopping_list[meal] = cost
            total_cost += cost
        else:
            print(f"Attention : Le repas '{meal}' est trop cher pour le budget restant.")
            break
            
    if total_cost > weekly_budget:
        return {"status": "budget_exceeded", "message": "Le plan de repas dépasse le budget alloué."}
    
    return {
        "shopping_list": list(shopping_list.keys()),
        "total_cost": round(total_cost, 2),
        "remaining_budget": round(weekly_budget - total_cost, 2)
    }

def generate_workout_plan(duration_minutes: int, focus_area: str) -> dict:
    """
    Génère un plan d'entraînement simple en fonction d'une durée et d'une zone de focus.
    
    Args:
        duration_minutes (int): Durée totale de l'entraînement en minutes.
        focus_area (str): La zone à travailler ('cardio', 'strength', 'stretching').
        
    Returns:
        dict: Un dictionnaire avec le plan d'entraînement détaillé.
    """
    if duration_minutes < 15:
        return {"error": "L'entraînement doit durer au moins 15 minutes."}

    warm_up_time = 5
    cool_down_time = 5
    workout_time = duration_minutes - warm_up_time - cool_down_time
    
    exercises = {
        "cardio": ["Jumping Jacks", "High Knees", "Burpees"],
        "strength": ["Push-ups", "Squats", "Plank"],
        "stretching": ["Hamstring Stretch", "Quad Stretch", "Triceps Stretch"]
    }
    
    plan = {
        "Warm-up": [f"Faire du jogging sur place pendant {warm_up_time} minutes."],
        "Workout": [],
        "Cool-down": [f"S'étirer pendant {cool_down_time} minutes."]
    }
    
    if focus_area.lower() in exercises:
        num_exercises = len(exercises[focus_area.lower()])
        time_per_exercise = workout_time / num_exercises
        
        for exercise in exercises[focus_area.lower()]:
            plan["Workout"].append(f"{exercise} : {int(time_per_exercise)} minutes.")
    else:
        plan["Workout"].append("Veuillez choisir une zone de focus valide.")
        
    return plan

def create_travel_itinerary(city: str, num_days: int) -> dict:
    """
    Crée un itinéraire de voyage de base pour une ville donnée sur plusieurs jours.
    
    Args:
        city (str): La ville de destination.
        num_days (int): La durée du séjour en jours.
        
    Returns:
        dict: Un itinéraire journalier avec des suggestions d'activités.
    """
    if num_days <= 0:
        return {"error": "Le séjour doit durer au moins un jour."}
        
    itinerary = {}
    city_activities = {
        "paris": ["Tour Eiffel", "Louvre", "Notre-Dame"],
        "new york": ["Statue de la Liberté", "Central Park", "Times Square"],
        "rome": ["Colisée", "Vatican", "Fontaine de Trevi"]
    }
    
    activities = city_activities.get(city.lower(), ["Activité touristique générale"])
    
    for day in range(1, num_days + 1):
        itinerary[f"Jour {day}"] = f"Explorer {random.choice(activities)}."
        
    return itinerary

def manage_task_list(task_list: list, action: str, task: str = None) -> list:
    """
    Gère une liste de tâches avec des actions 'add', 'remove' et 'show'.
    
    Args:
        task_list (list): La liste de tâches actuelle.
        action (str): L'action à effectuer ('add', 'remove', 'show').
        task (str, optional): La tâche à ajouter ou à supprimer.
        
    Returns:
        list: La nouvelle liste de tâches.
    """
    if action == "add" and task:
        if task not in task_list:
            task_list.append(task)
            print(f"Tâche '{task}' ajoutée.")
        else:
            print(f"La tâche '{task}' existe déjà.")
    elif action == "remove" and task:
        if task in task_list:
            task_list.remove(task)
            print(f"Tâche '{task}' retirée.")
        else:
            print(f"La tâche '{task}' n'existe pas.")
    elif action == "show":
        print("Liste de tâches actuelle :")
        for i, item in enumerate(task_list):
            print(f"  {i+1}. {item}")
    else:
        print("Action ou tâche invalide.")
        
    return task_list

# Exemple d'utilisation
if __name__ == "__main__":
    
    # --- Exemples de fonctions courtes ---
    print("--- Test des fonctions courtes ---")
    tip = calculate_tip(50.0, 20)
    print(f"Pour un repas de 50€, un pourboire de 20% est de {tip}€.")
    
    prime_check = is_prime(17)
    print(f"Est-ce que 17 est un nombre premier ? {prime_check}")
    
    # --- Exemples de fonctions plus larges ---
    print("\n--- Test des fonctions plus larges ---")
    
    mon_budget = 100
    mon_plan_repas = {
        "Steak frites": 25,
        "Poulet rôti": 35,
        "Légumes": 15,
        "Dessert": 10
    }
    plan_courses = plan_weekly_groceries(mon_budget, mon_plan_repas)
    print(f"Plan de courses : {plan_courses}")
    
    plan_entrainement = generate_workout_plan(duration_minutes=30, focus_area="cardio")
    print("\nPlan d'entraînement de 30 minutes :")
    for section, exercises in plan_entrainement.items():
        print(f"  - {section} : {exercises}")
    
    # Gestion d'une liste de tâches
    ma_liste = ["Acheter du lait", "Payer les factures"]
    ma_liste = manage_task_list(ma_liste, "add", "Appeler un ami")
    ma_liste = manage_task_list(ma_liste, "show")
