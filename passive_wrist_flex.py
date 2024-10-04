import time
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import os

# Fonction pour convertir du texte en audio et ajouter un intervalle
def text_to_speech_with_pause(text, interval, output_file):
    tts = gTTS(text, lang='fr')
    temp_file = "temp.mp3"
    tts.save(temp_file)
    
    audio = AudioSegment.from_mp3(temp_file)
    pause = AudioSegment.silent(duration=interval * 1000)
    final_audio = audio + pause
    
    final_audio.export(output_file, format="mp3")
    os.remove(temp_file)
    
    return final_audio

# Fonction pour ajouter plusieurs répétitions avec des pauses
def repeat_instructions(texts, intervals, repetitions):
    combined_audio = AudioSegment.silent(duration=0)
    
    for _ in range(repetitions):
        for i, text in enumerate(texts):
            output = f"output_part_{i}.mp3"
            audio_with_pause = text_to_speech_with_pause(text, intervals[i], output)
            combined_audio += audio_with_pause
    
    return combined_audio

# Fonction principale pour créer un exercice
def create_exercise(exercise_name, description, debut_exercise, instructions, intervals, repetitions, output_file):
    text_to_speech_with_pause(exercise_name, 1, "nom_exercice.mp3")
    text_to_speech_with_pause(description, 3, "description.mp3")
    text_to_speech_with_pause(debut_exercise, 2, "debut_exercice.mp3")
    
    final_audio = AudioSegment.silent(duration=0)
    final_audio += AudioSegment.from_mp3("nom_exercice.mp3")
    final_audio += AudioSegment.from_mp3("description.mp3")
    final_audio += AudioSegment.from_mp3("debut_exercice.mp3")
    
    repeated_audio = repeat_instructions(instructions, intervals, repetitions)
    final_audio += repeated_audio
    
    final_audio.export(output_file, format="mp3")
    print(f"Audio for {exercise_name} saved as {output_file}")
    
    os.remove("nom_exercice.mp3")
    os.remove("description.mp3")
    os.remove("debut_exercice.mp3")

# Fonction pour ajouter une musique d'ambiance à toute la séance
def add_background_music_to_session(session_audio_file, music_file, output_file, music_volume=-20):
    # Charger l'audio de la séance et la musique d'ambiance
    session_audio = AudioSegment.from_mp3(session_audio_file)
    music = AudioSegment.from_mp3(music_file)
    
    # Ajuster le volume de la musique (ex: -20 dB pour une musique en arrière-plan)
    music = music - abs(music_volume)
    
    # Répéter la musique pour qu'elle dure aussi longtemps que la séance
    if len(music) < len(session_audio):
        music = music * (len(session_audio) // len(music) + 1)
    
    # Couper la musique pour qu'elle corresponde à la durée de la séance
    music = music[:len(session_audio)]
    
    # Superposer la musique d'ambiance sur l'audio de la séance
    final_audio = session_audio.overlay(music)
    
    # Sauvegarder l'audio final avec la musique
    final_audio.export(output_file, format="mp3")
    print(f"Final audio with background music saved as {output_file}")

# Créer le fichier global du programme
def create_program_with_title(title, exercises, output_file):
    text_to_speech_with_pause(title, 2, "titre.mp3")
    
    final_audio = AudioSegment.silent(duration=0)
    final_audio += AudioSegment.from_mp3("titre.mp3")
    
    for exercise in exercises:
        exercise_audio = AudioSegment.from_mp3(exercise['file'])
        final_audio += exercise_audio
    
    final_audio.export(output_file, format="mp3")
    print(f"Programme complet saved as {output_file}")
    
    os.remove("titre.mp3")

# Liste des exercices
exercises = []

# Exercice de flexion
create_exercise(
    exercise_name="Flexion",
    description="Déposer le poignet sur le bord d'une table. Avec la main opposée, plier le poignet aussi loin que possible. Relâcher et recommencer.",
    debut_exercise="Commencer la flexion.",
    instructions=["Maintenir", "Relâcher"],
    intervals=[15, 3],  # Intervalles en secondes
    repetitions=15,     # Nombre de répétitions
    output_file="exercice_flexion.mp3"
)
exercises.append({'name': 'Flexion', 'file': "exercice_flexion.mp3"})

# Exercice de prière
create_exercise(
    exercise_name="Prière",
    description="Joindre les paumes ensemble à la façon d'une prière. Tout en gardant les paumes collées, descendre les mains jusqu'à la hauteur des coudes. Relâcher et recommencer.",	
    debut_exercise="Commencer la prière.",
    instructions=["Maintenir", "Relâcher"],
    intervals=[5, 2],  # Intervalles en secondes
    repetitions=10,     # Nombre de répétitions
    output_file="exercice_priere.mp3"
)
exercises.append({'name': 'Priere', 'file': "exercice_priere.mp3"})

# Exercice d'extension sur une table'
create_exercise(
    exercise_name="Extension sur une table",
    description="Déposer les mains à plat sur le bord d'une table. Sans plier les coudes, incliner le corps vers l'avant pour étirer les poignets. Relâcher et recommencer.",	
    debut_exercise="Commencer l'extension.",
    instructions=["Maintenir", "Relâcher"],
    intervals=[30, 5],  # Intervalles en secondes
    repetitions=5,     # Nombre de répétitions
    output_file="exercice_extension.mp3"
)
exercises.append({'name': 'Extension', 'file': "exercice_extension.mp3"})

# Exercice de déviation radio-ulnaire'
create_exercise(
    exercise_name="Déviation radio-ulnaire",
    description="Déposer l'avant-bras sur une table, pouce vers le haut, en laissant dépasser le poignet. En tenant fermement un marteau ou un poids, incliner la main vers le bas sans décoller le couder de la table. Ensuite, ramener la main vers le haut sans décoller l'avant-bras de la table.",	
    debut_exercise="Commencer la déviation.",
    instructions=["Incliner", "Ramener"],
    intervals=[5, 2],  # Intervalles en secondes
    repetitions=15,     # Nombre de répétitions
    output_file="exercice_deviation.mp3"
)
exercises.append({'name': 'Deviation', 'file': "exercice_deviation.mp3"})

# Créer le programme complet avec le titre une seule fois au début
create_program_with_title(
    title="Programme d'exercices passifs du poignet",
    exercises=exercises,
    output_file="programme_exercice_complet.mp3"
)

# Ajouter la musique d'ambiance à toute la séance
add_background_music_to_session(
    session_audio_file="programme_exercice_complet.mp3", 
    music_file="ambiance_music.mp3",  # Musique d'ambiance
    output_file="programme_exercice_complet_avec_musique.mp3", 
    music_volume=-20  # Réduire le volume de la musique
)
