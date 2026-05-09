#!/usr/bin/env python3
"""
Guía Interactiva para CTF (Capture The Flag)
Herramienta para documentar paso a paso la resolución de desafíos de ciberseguridad
"""

import json
import datetime
import os
import sys
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict
from enum import Enum

class CTFCategory(Enum):
    WEB = "Web Exploitation"
    CRYPTO = "Cryptography"
    REVERSE = "Reverse Engineering"
    FORENSICS = "Digital Forensics"
    PWNING = "Binary Exploitation"
    STEGANOGRAPHY = "Steganography"
    MISC = "Miscellaneous"
    OSINT = "Open Source Intelligence"

@dataclass
class CTFStep:
    step_number: int
    category: str
    description: str
    command: str
    output: str
    findings: str
    timestamp: str
    difficulty: str
    hints: List[str]
    
@dataclass
class CTFChallenge:
    name: str
    category: str
    difficulty: str
    description: str
    flag: str
    start_time: str
    end_time: str
    steps: List[CTFStep]
    tools_used: List[str]
    techniques: List[str]
    learning_points: List[str]
    total_time: str

class CTFGuide:
    def __init__(self):
        self.current_challenge: Optional[CTFChallenge] = None
        self.completed_challenges: List[CTFChallenge] = []
        self.current_step = 0
        
    def show_banner(self):
        """Muestra el banner de la aplicación"""
        print("\n" + "="*60)
        print("🚩 GUÍA INTERACTIVA CTF - CAPTURE THE FLAG 🚩")
        print("="*60)
        print("Documenta tu proceso paso a paso y genera informes detallados")
        print("="*60 + "\n")
    
    def show_categories(self):
        """Muestra las categorías disponibles"""
        print("\n📂 CATEGORÍAS DISPONIBLES:")
        print("-" * 40)
        for i, category in enumerate(CTFCategory, 1):
            print(f"{i}. {category.value}")
        print("-" * 40)
    
    def create_new_challenge(self):
        """Crea un nuevo desafío CTF"""
        self.show_banner()
        print("🔥 CREANDO NUEVO DESAFÍO CTF")
        print("-" * 30)
        
        name = input("Nombre del desafío: ").strip()
        if not name:
            print("❌ El nombre no puede estar vacío")
            return
        
        description = input("Descripción del desafío: ").strip()
        
        self.show_categories()
        try:
            cat_choice = int(input("Selecciona categoría (1-8): ")) - 1
            category = list(CTFCategory)[cat_choice].value
        except (ValueError, IndexError):
            print("❌ Selección inválida, usando 'Miscellaneous'")
            category = CTFCategory.MISC.value
        
        difficulty = input("Dificultad (Easy/Medium/Hard): ").strip() or "Medium"
        
        self.current_challenge = CTFChallenge(
            name=name,
            category=category,
            difficulty=difficulty,
            description=description,
            flag="",
            start_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            end_time="",
            steps=[],
            tools_used=[],
            techniques=[],
            learning_points=[],
            total_time=""
        )
        
        self.current_step = 0
        print(f"\n✅ Desafío '{name}' creado exitosamente!")
        print(f"📂 Categoría: {category}")
        print(f"⚡ Dificultad: {difficulty}")
        
    def add_step(self):
        """Añade un paso al desafío actual"""
        if not self.current_challenge:
            print("❌ No hay desafío activo. Crea uno primero.")
            return
        
        self.current_step += 1
        print(f"\n📝 PASO {self.current_step}")
        print("-" * 30)
        
        description = input("Descripción del paso: ").strip()
        if not description:
            print("❌ La descripción no puede estar vacía")
            return
        
        command = input("Comando/Herramienta utilizada: ").strip()
        output = input("Resultado/Output obtenido: ").strip()
        findings = input("Hallazgos importantes: ").strip()
        difficulty = input("Dificultad del paso (Easy/Medium/Hard): ").strip() or "Medium"
        
        # Recopilar hints
        hints = []
        print("\n💡 Añade hints para este paso (Enter vacío para terminar):")
        while True:
            hint = input(f"Hint {len(hints) + 1}: ").strip()
            if not hint:
                break
            hints.append(hint)
        
        step = CTFStep(
            step_number=self.current_step,
            category=self.current_challenge.category,
            description=description,
            command=command,
            output=output,
            findings=findings,
            timestamp=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            difficulty=difficulty,
            hints=hints
        )
        
        self.current_challenge.steps.append(step)
        
        # Actualizar herramientas utilizadas
        if command and command not in self.current_challenge.tools_used:
            self.current_challenge.tools_used.append(command)
        
        print(f"✅ Paso {self.current_step} añadido exitosamente!")
    
    def finish_challenge(self):
        """Finaliza el desafío actual"""
        if not self.current_challenge:
            print("❌ No hay desafío activo.")
            return
        
        print(f"\n🏁 FINALIZANDO DESAFÍO: {self.current_challenge.name}")
        print("-" * 50)
        
        flag = input("Flag obtenida: ").strip()
        self.current_challenge.flag = flag
        
        # Recopilar técnicas utilizadas
        print("\n🔧 Técnicas utilizadas (Enter vacío para terminar):")
        while True:
            technique = input(f"Técnica {len(self.current_challenge.techniques) + 1}: ").strip()
            if not technique:
                break
            self.current_challenge.techniques.append(technique)
        
        # Recopilar puntos de aprendizaje
        print("\n🎓 Puntos de aprendizaje (Enter vacío para terminar):")
        while True:
            learning = input(f"Aprendizaje {len(self.current_challenge.learning_points) + 1}: ").strip()
            if not learning:
                break
            self.current_challenge.learning_points.append(learning)
        
        # Calcular tiempo total
        end_time = datetime.datetime.now()
        self.current_challenge.end_time = end_time.strftime("%Y-%m-%d %H:%M:%S")
        
        start_dt = datetime.datetime.strptime(self.current_challenge.start_time, "%Y-%m-%d %H:%M:%S")
        total_seconds = (end_time - start_dt).total_seconds()
        hours = int(total_seconds // 3600)
        minutes = int((total_seconds % 3600) // 60)
        self.current_challenge.total_time = f"{hours}h {minutes}m"
        
        # Guardar desafío completado
        self.completed_challenges.append(self.current_challenge)
        print(f"✅ Desafío completado en {self.current_challenge.total_time}")
        
        self.current_challenge = None
        self.current_step = 0
    
    def view_current_progress(self):
        """Muestra el progreso actual del desafío"""
        if not self.current_challenge:
            print("❌ No hay desafío activo.")
            return
        
        print(f"\n📊 PROGRESO ACTUAL")
        print("=" * 50)
        print(f"🚩 Desafío: {self.current_challenge.name}")
        print(f"📂 Categoría: {self.current_challenge.category}")
        print(f"⚡ Dificultad: {self.current_challenge.difficulty}")
        print(f"🕒 Inicio: {self.current_challenge.start_time}")
        print(f"📝 Pasos completados: {len(self.current_challenge.steps)}")
        
        if self.current_challenge.steps:
            print(f"\n📋 RESUMEN DE PASOS:")
            for step in self.current_challenge.steps:
                print(f"  {step.step_number}. {step.description}")
                if step.findings:
                    print(f"     💡 Hallazgos: {step.findings}")
        
        print(f"\n🔧 Herramientas utilizadas: {', '.join(self.current_challenge.tools_used)}")
    
    def export_report(self, format_type="txt"):
        """Exporta un informe de todos los desafíos completados"""
        if not self.completed_challenges:
            print("❌ No hay desafíos completados para exportar.")
            return
        
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"ctf_report_{timestamp}.{format_type}"
        
        try:
            if format_type == "txt":
                self._export_txt_report(filename)
            elif format_type == "json":
                self._export_json_report(filename)
            elif format_type == "html":
                self._export_html_report(filename)
            else:
                print("❌ Formato no soportado. Usa 'txt', 'json' o 'html'")
                return
            
            print(f"✅ Informe exportado exitosamente: {filename}")
            
        except Exception as e:
            print(f"❌ Error al exportar: {str(e)}")
    
    def _export_txt_report(self, filename):
        """Exporta informe en formato texto"""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("🚩 INFORME DE DESAFÍOS CTF\n")
            f.write("=" * 60 + "\n\n")
            f.write(f"Generado el: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Total de desafíos: {len(self.completed_challenges)}\n\n")
            
            for i, challenge in enumerate(self.completed_challenges, 1):
                f.write(f"DESAFÍO {i}: {challenge.name}\n")
                f.write("-" * 50 + "\n")
                f.write(f"Categoría: {challenge.category}\n")
                f.write(f"Dificultad: {challenge.difficulty}\n")
                f.write(f"Descripción: {challenge.description}\n")
                f.write(f"Flag: {challenge.flag}\n")
                f.write(f"Tiempo total: {challenge.total_time}\n")
                f.write(f"Inicio: {challenge.start_time}\n")
                f.write(f"Fin: {challenge.end_time}\n\n")
                
                f.write("PASOS SEGUIDOS:\n")
                for step in challenge.steps:
                    f.write(f"  {step.step_number}. {step.description}\n")
                    f.write(f"     Comando: {step.command}\n")
                    f.write(f"     Resultado: {step.output}\n")
                    f.write(f"     Hallazgos: {step.findings}\n")
                    f.write(f"     Timestamp: {step.timestamp}\n")
                    if step.hints:
                        f.write(f"     Hints: {', '.join(step.hints)}\n")
                    f.write("\n")
                
                f.write(f"HERRAMIENTAS UTILIZADAS: {', '.join(challenge.tools_used)}\n")
                f.write(f"TÉCNICAS APLICADAS: {', '.join(challenge.techniques)}\n")
                f.write(f"PUNTOS DE APRENDIZAJE: {', '.join(challenge.learning_points)}\n\n")
                f.write("=" * 60 + "\n\n")
    
    def _export_json_report(self, filename):
        """Exporta informe en formato JSON"""
        report_data = {
            "generated_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "total_challenges": len(self.completed_challenges),
            "challenges": [asdict(challenge) for challenge in self.completed_challenges]
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(report_data, f, indent=2, ensure_ascii=False)
    
    def _export_html_report(self, filename):
        """Exporta informe en formato HTML"""
        html_content = f"""
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Informe CTF</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; background-color: #f5f5f5; }}
                .container {{ max-width: 1000px; margin: 0 auto; background: white; padding: 20px; border-radius: 10px; }}
                .header {{ text-align: center; color: #333; border-bottom: 2px solid #007acc; padding-bottom: 10px; }}
                .challenge {{ margin: 20px 0; padding: 15px; border: 1px solid #ddd; border-radius: 5px; }}
                .step {{ margin: 10px 0; padding: 10px; background: #f9f9f9; border-left: 4px solid #007acc; }}
                .flag {{ color: #d9534f; font-weight: bold; }}
                .tools {{ color: #5cb85c; }}
                .techniques {{ color: #f0ad4e; }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>🚩 Informe de Desafíos CTF</h1>
                    <p>Generado el: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
                    <p>Total de desafíos: {len(self.completed_challenges)}</p>
                </div>
        """
        
        for i, challenge in enumerate(self.completed_challenges, 1):
            html_content += f"""
                <div class="challenge">
                    <h2>Desafío {i}: {challenge.name}</h2>
                    <p><strong>Categoría:</strong> {challenge.category}</p>
                    <p><strong>Dificultad:</strong> {challenge.difficulty}</p>
                    <p><strong>Descripción:</strong> {challenge.description}</p>
                    <p class="flag"><strong>Flag:</strong> {challenge.flag}</p>
                    <p><strong>Tiempo total:</strong> {challenge.total_time}</p>
                    
                    <h3>Pasos seguidos:</h3>
            """
            
            for step in challenge.steps:
                html_content += f"""
                    <div class="step">
                        <h4>Paso {step.step_number}: {step.description}</h4>
                        <p><strong>Comando:</strong> <code>{step.command}</code></p>
                        <p><strong>Resultado:</strong> {step.output}</p>
                        <p><strong>Hallazgos:</strong> {step.findings}</p>
                        <p><strong>Timestamp:</strong> {step.timestamp}</p>
                        {f"<p><strong>Hints:</strong> {', '.join(step.hints)}</p>" if step.hints else ""}
                    </div>
                """
            
            html_content += f"""
                    <p class="tools"><strong>Herramientas utilizadas:</strong> {', '.join(challenge.tools_used)}</p>
                    <p class="techniques"><strong>Técnicas aplicadas:</strong> {', '.join(challenge.techniques)}</p>
                    <p><strong>Puntos de aprendizaje:</strong> {', '.join(challenge.learning_points)}</p>
                </div>
            """
        
        html_content += """
            </div>
        </body>
        </html>
        """
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
    
    def show_menu(self):
        """Muestra el menú principal"""
        print("\n🎯 MENÚ PRINCIPAL")
        print("-" * 30)
        print("1. Crear nuevo desafío")
        print("2. Añadir paso")
        print("3. Ver progreso actual")
        print("4. Finalizar desafío")
        print("5. Exportar informe (TXT)")
        print("6. Exportar informe (JSON)")
        print("7. Exportar informe (HTML)")
        print("8. Ver desafíos completados")
        print("9. Ayuda")
        print("0. Salir")
        print("-" * 30)
    
    def show_completed_challenges(self):
        """Muestra todos los desafíos completados"""
        if not self.completed_challenges:
            print("❌ No hay desafíos completados.")
            return
        
        print(f"\n🏆 DESAFÍOS COMPLETADOS ({len(self.completed_challenges)})")
        print("=" * 50)
        
        for i, challenge in enumerate(self.completed_challenges, 1):
            print(f"{i}. {challenge.name}")
            print(f"   📂 {challenge.category} | ⚡ {challenge.difficulty}")
            print(f"   🚩 Flag: {challenge.flag}")
            print(f"   ⏱️ Tiempo: {challenge.total_time}")
            print(f"   📝 Pasos: {len(challenge.steps)}")
            print("-" * 50)
    
    def show_help(self):
        """Muestra la ayuda del sistema"""
        print("\n📖 AYUDA - GUÍA INTERACTIVA CTF")
        print("=" * 50)
        print("Esta herramienta te ayuda a documentar tu proceso de resolución")
        print("de desafíos CTF paso a paso y generar informes detallados.")
        print()
        print("🔄 FLUJO DE TRABAJO:")
        print("1. Crea un nuevo desafío")
        print("2. Añade pasos conforme resuelves")
        print("3. Documenta comandos, resultados y hallazgos")
        print("4. Finaliza el desafío cuando obtengas la flag")
        print("5. Exporta informes en diferentes formatos")
        print()
        print("💡 CONSEJOS:")
        print("• Sé detallado en las descripciones")
        print("• Documenta todos los comandos utilizados")
        print("• Anota los hallazgos importantes")
        print("• Añade hints para futuras referencias")
        print("• Exporta regularmente tus informes")
        print("=" * 50)
    
    def run(self):
        """Ejecuta la aplicación principal"""
        self.show_banner()
        
        while True:
            self.show_menu()
            
            try:
                choice = input("\nSelecciona una opción: ").strip()
                
                if choice == '1':
                    self.create_new_challenge()
                elif choice == '2':
                    self.add_step()
                elif choice == '3':
                    self.view_current_progress()
                elif choice == '4':
                    self.finish_challenge()
                elif choice == '5':
                    self.export_report('txt')
                elif choice == '6':
                    self.export_report('json')
                elif choice == '7':
                    self.export_report('html')
                elif choice == '8':
                    self.show_completed_challenges()
                elif choice == '9':
                    self.show_help()
                elif choice == '0':
                    print("\n👋 ¡Hasta luego! Happy hacking!")
                    break
                else:
                    print("❌ Opción inválida. Intenta nuevamente.")
                    
            except KeyboardInterrupt:
                print("\n\n👋 ¡Hasta luego! Happy hacking!")
                break
            except Exception as e:
                print(f"❌ Error inesperado: {str(e)}")

def main():
    """Función principal"""
    try:
        guide = CTFGuide()
        guide.run()
    except Exception as e:
        print(f"❌ Error crítico: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
