from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configuración del driver de Edge
service = Service(executable_path=r"C:\drivers\msedgedriver.exe")
driver = webdriver.Edge(service=service)
driver.maximize_window()

try:
    print("=== INICIANDO CP-04: Login Exitoso ===")
    
    # Paso 1: Ir a Coursera
    print("\nPaso 1: Navegando a Coursera...")
    driver.get("https://www.coursera.org")
    time.sleep(5)
    driver.save_screenshot(r"D:\Universidad\Semestre5\Administracion\coursera_selenium\evidencias\cp04\paso1_pagina_principal.png")
    print("✓ Captura guardada: paso1_pagina_principal.png")
    
    # Paso 2: Clic en Log In
    print("\nPaso 2: Buscando botón Log In...")
    try:
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Log In"))
        )
        login_button.click()
        print("✓ Botón 'Log In' clickeado")
    except:
        print("⚠ No se encontró botón, yendo directamente a login...")
        driver.get("https://www.coursera.org/?authMode=login")
    
    time.sleep(4)
    driver.save_screenshot(r"D:\Universidad\Semestre5\Administracion\coursera_selenium\evidencias\cp04\paso2_pagina_login.png")
    print("✓ Captura guardada: paso2_pagina_login.png")
    
    # Paso 3: Ingresar EMAIL
    print("\nPaso 3: Ingresando email...")
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "email"))
    )
    email_field.clear()
    email_field.send_keys("teste.courser0909@gmail.com")
    time.sleep(2)
    driver.save_screenshot(r"D:\Universidad\Semestre5\Administracion\coursera_selenium\evidencias\cp04\paso3_email_ingresado.png")
    print("✓ Email ingresado: teste.courser0909@gmail.com")
    print("✓ Captura guardada: paso3_email_ingresado.png")
    
    # Paso 4: Clic en CONTINUAR
    print("\nPaso 4: Haciendo clic en botón 'Continuar'...")
    continue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.css-hsv6bp[type='submit']"))
    )
    continue_button.click()
    time.sleep(3)
    driver.save_screenshot(r"D:\Universidad\Semestre5\Administracion\coursera_selenium\evidencias\cp04\paso4_continue_clickeado.png")
    print("✓ Botón 'Continuar' clickeado")
    print("✓ Captura guardada: paso4_continue_clickeado.png")
    
    # Paso 5: Ingresar CONTRASEÑA
    print("\nPaso 5: Ingresando contraseña...")
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-e2e='login-password-input']"))
    )
    password_field.clear()
    password_field.send_keys("TESTEANDO_COURSERA56")
    time.sleep(2)
    driver.save_screenshot(r"D:\Universidad\Semestre5\Administracion\coursera_selenium\evidencias\cp04\paso5_password_ingresado.png")
    print("✓ Contraseña ingresada")
    print("✓ Captura guardada: paso5_password_ingresado.png")
    
    # Paso 6: Clic en botón SIGUIENTE (LOG IN FINAL)
    print("\nPaso 6: Haciendo clic en botón 'Siguiente'...")
    login_final_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-e2e='login-form-submit-button']"))
    )
    login_final_button.click()
    time.sleep(8)
    driver.save_screenshot(r"D:\Universidad\Semestre5\Administracion\coursera_selenium\evidencias\cp04\paso6_login_exitoso.png")
    print("✓ Botón 'Siguiente' clickeado")
    print("✓ Captura guardada: paso6_login_exitoso.png")
    
    # Validación: Verificar que el login fue exitoso
    print("\n" + "="*60)
    print("VALIDANDO LOGIN...")
    print("="*60)
    time.sleep(3)
    
    current_url = driver.current_url
    print(f"URL actual: {current_url}")
    
    if "login" not in current_url.lower() and "authmode" not in current_url.lower():
        print("✓✓✓ LOGIN EXITOSO - Ya no estamos en página de login")
    else:
        print("⚠ Aún en página de login - Verificar credenciales")
    
    # Captura final de la página después de login
    driver.save_screenshot(r"D:\Universidad\Semestre5\Administracion\coursera_selenium\evidencias\cp04\paso7_validacion_final.png")
    print("✓ Captura guardada: paso7_validacion_final.png")
    
    print("\n" + "="*60)
    print("✓✓✓ CP-04 COMPLETADO EXITOSAMENTE ✓✓✓")
    print("="*60)
    
except Exception as e:
    print("\n" + "="*60)
    print("✗✗✗ ERROR en CP-04 ✗✗✗")
    print("="*60)
    print(f"Error detallado: {str(e)}")
    print(f"URL actual al momento del error: {driver.current_url}")
    driver.save_screenshot(r"D:\Universidad\Semestre5\Administracion\coursera_selenium\evidencias\cp04\error.png")
    print("✓ Captura de error guardada: error.png")
    
finally:
    print("\nEsperando 8 segundos antes de cerrar para que veas el resultado...")
    time.sleep(8)
    driver.quit()
    print("\n=== FIN DE CP-04 ===\n")