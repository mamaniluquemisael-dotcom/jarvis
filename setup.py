#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script de instalación y configuración rápida para JARVIS
"""

import os
import sys
import platform
import subprocess

def run_command(command):
    """Ejecuta un comando en terminal"""
    try:
        subprocess.run(command, shell=True, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    print("\n" + "="*70)
    print("🤖 JARVIS - Setup Wizard")
    print("="*70)
    
    print("\n📋 Verificando requisitos...")
    
    # Verificar Python
    print(f"✓ Python {sys.version.split()[0]}")
    
    # Crear .env si no existe
    if not os.path.exists('.env'):
        print("\n📝 Creando archivo .env...")
        if os.path.exists('.env.example'):
            run_command('copy .env.example .env' if platform.system() == 'Windows' else 'cp .env.example .env')
            print("✓ Archivo .env creado")
        else:
            print("⚠️  Archivo .env.example no encontrado")
    else:
        print("✓ Archivo .env ya existe")
    
    # Instalar dependencias
    print("\n📦 Instalando dependencias...")
    print("\n¿Qué deseas instalar?")
    print("1. Solo CLI (JARVIS + Tareas)")
    print("2. Solo Web (Flask)")
    print("3. Todo (CLI + Web)")
    
    choice = input("\nOpción (1-3): ").strip()
    
    if choice in ['1', '3']:
        print("\nInstalando dependencias CLI...")
        run_command('pip install -r requirements.txt')
    
    if choice in ['2', '3']:
        print("\nInstalando dependencias Web...")
        run_command('pip install -r requirements_web.txt')
    
    # Configurar API Key
    print("\n🔑 Configurar API Key de Groq")
    print("1. Si ya tienes una key, edita .env")
    print("2. Si no, ve a https://console.groq.com")
    
    # Crear directorio de datos si no existe
    if not os.path.exists('data'):
        os.makedirs('data')
        print("\n✓ Carpeta 'data' creada")
    
    print("\n" + "="*70)
    print("✨ ¡Instalación completada!")
    print("="*70)
    
    print("\n🚀 Próximos pasos:")
    print("\n1. Edita .env con tu API Key de Groq")
    print("\n2. Para usar JARVIS (CLI):")
    print("   python jarvis.py")
    print("\n3. Para usar Gestor de Tareas (CLI):")
    print("   python todo_app.py")
    print("\n4. Para usar versión Web:")
    print("   python app.py")
    print("   Luego abre http://localhost:5000")
    print("\n" + "="*70)

if __name__ == '__main__':
    main()
