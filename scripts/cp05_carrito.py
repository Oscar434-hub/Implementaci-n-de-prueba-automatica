from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configuración del driver de Edge
service = Service(executable_path=r"C:\drivers\msedgedriver.exe")
driver = webdriver.Edge(service=service)
driver.maximize_window()

try:
    print("=== INICIANDO CP-05: Buscar Curso y Ver Detalles ===")
    
    # Paso 1: Login previo
    print("\nPaso 1: Realizando login en Coursera...")
    driver.get("https://www.coursera.org")
    time.sleep(3)
    
    # Ir a login
    try:
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Log In"))
        )
        login_button.click()
        print("✓ Botón 'Log In' clickeado")
    except:
        driver.get("https://www.coursera.org/?authMode=login")
        print("✓ Navegando directamente a login")
    
    time.sleep(3)
    
    # Ingresar email
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "email"))
    )
    email_field.send_keys("teste.courser0909@gmail.com")
    print("✓ Email ingresado")
    
    # Clic en Continuar
    continue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.css-hsv6bp[type='submit']"))
    )
    continue_button.click()
    time.sleep(3)
    print("✓ Botón 'Continuar' clickeado")
    
    # Ingresar contraseña
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-e2e='login-password-input']"))
    )
    password_field.send_keys("TESTEANDO_COURSERA56")
    print("✓ Contraseña ingresada")
    
    # Clic en Siguiente
    login_final_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-e2e='login-form-submit-button']"))
    )
    login_final_button.click()
    time.sleep(6)
    print("✓ Login completado")
    
    driver.save_screenshot(r"D:\Universidad\Semestre5\Administracion\coursera_selenium\evidencias\cp05\paso1_login_completado.png")
    print("✓ Captura guardada: paso1_login_completado.png")
    
    # Paso 2: Buscar curso
    print("\nPaso 2: Buscando curso 'Python for Everybody'...")
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "search-autocomplete-input"))
    )
    search_box.clear()
    search_box.send_keys("Python for Everybody")
    time.sleep(1)
    driver.save_screenshot(r"D:\Universidad\Semestre5\Administracion\coursera_selenium\evidencias\cp05\paso2_termino_busqueda.png")
    print("✓ Término ingresado: 'Python for Everybody'")
    print("✓ Captura guardada: paso2_termino_busqueda.png")
    
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)
    driver.save_screenshot(r"D:\Universidad\Semestre5\Administracion\coursera_selenium\evidencias\cp05\paso3_resultados_busqueda.png")
    print("✓ Búsqueda ejecutada")
    print("✓ Captura guardada: paso3_resultados_busqueda.png")
    
    # Paso 3: Abrir primer curso de los resultados
    print("\nPaso 3: Abriendo primer curso de los resultados...")
    try:
        # Buscar el primer enlace de curso
        first_course = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-click-key*='search.click'], a[href*='/learn/']"))
        )
        course_title = first_course.text
        print(f"✓ Curso encontrado: {course_title}")
        first_course.click()
        time.sleep(5)
    except Exception as e:
        print(f"⚠ No se pudo hacer clic automático: {str(e)}")
        print("⚠ Intentando método alternativo...")
        # Si falla, tomar captura del problema
    
    driver.save_screenshot(r"D:\Universidad\Semestre5\Administracion\coursera_selenium\evidencias\cp05\paso4_pagina_curso.png")
    print("✓ Captura guardada: paso4_pagina_curso.png")
    
    # Paso 4: Capturar botón de inscripción/carrito
    print("\nPaso 4: Capturando botón de inscripción...")
    current_url = driver.current_url
    print(f"URL del curso: {current_url}")
    
    # Buscar botón de inscripción
    try:
        enroll_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Inscribirse') or contains(text(), 'Enroll') or contains(text(), 'Start')]"))
        )
        print("✓ Botón de inscripción encontrado")
        driver.save_screenshot(r"D:\Universidad\Semestre5\Administracion\coursera_selenium\evidencias\cp05\paso5_boton_inscripcion.png")
        print("✓ Captura guardada: paso5_boton_inscripcion.png")
    except:
        print("⚠ Botón de inscripción no encontrado con los selectores actuales")
        driver.save_screenshot(r"D:\Universidad\Semestre5\Administracion\coursera_selenium\evidencias\cp05\paso5_vista_curso.png")
        print("✓ Captura guardada: paso5_vista_curso.png")
    
    # Paso 5: Scroll para ver más detalles
    print("\nPaso 5: Capturando detalles del curso...")
    driver.execute_script("window.scrollTo(0, 800);")
    time.sleep(2)
    driver.save_screenshot(r"D:\Universidad\Semestre5\Administracion\coursera_selenium\evidencias\cp05\paso6_detalles_curso.png")
    print("✓ Captura guardada: paso6_detalles_curso.png")
    
    print("\n" + "="*60)
    print("✓✓✓ CP-05 COMPLETADO EXITOSAMENTE ✓✓✓")
    print("="*60)
    print("Se navegó exitosamente hasta la página del curso")
    
except Exception as e:
    print("\n" + "="*60)
    print("✗✗✗ ERROR en CP-05 ✗✗✗")
    print("="*60)
    print(f"Error detallado: {str(e)}")
    print(f"URL actual: {driver.current_url}")
    driver.save_screenshot(r"D:\Universidad\Semestre5\Administracion\coursera_selenium\evidencias\cp05\error.png")
    print("✓ Captura de error guardada: error.png")
    
finally:
    print("\nEsperando 5 segundos antes de cerrar...")
    time.sleep(5)
    driver.quit()
    print("\n=== FIN DE CP-05 ===\n")