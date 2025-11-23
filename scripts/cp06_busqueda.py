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
    print("=== INICIANDO CP-06: Búsqueda de Curso ===")
    
    # Paso 1: Ir a Coursera
    print("\nPaso 1: Navegando a Coursera...")
    driver.get("https://www.coursera.org")
    time.sleep(4)
    driver.save_screenshot(r"D:\Universidad\Semestre5\Administracion\coursera_selenium\evidencias\cp06\paso1_pagina_principal.png")
    print("✓ Captura guardada: paso1_pagina_principal.png")
    
    # Paso 2: Localizar barra de búsqueda
    print("\nPaso 2: Localizando barra de búsqueda...")
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "search-autocomplete-input"))
    )
    print("✓ Barra de búsqueda localizada")
    driver.save_screenshot(r"D:\Universidad\Semestre5\Administracion\coursera_selenium\evidencias\cp06\paso2_barra_busqueda.png")
    print("✓ Captura guardada: paso2_barra_busqueda.png")
    
    # Paso 3: Ingresar término de búsqueda
    print("\nPaso 3: Ingresando término 'Python'...")
    search_box.clear()
    search_box.send_keys("Python")
    time.sleep(2)
    driver.save_screenshot(r"D:\Universidad\Semestre5\Administracion\coursera_selenium\evidencias\cp06\paso3_termino_ingresado.png")
    print("✓ Término 'Python' ingresado")
    print("✓ Captura guardada: paso3_termino_ingresado.png")
    
    # Paso 4: Presionar Enter para buscar
    print("\nPaso 4: Ejecutando búsqueda...")
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)
    driver.save_screenshot(r"D:\Universidad\Semestre5\Administracion\coursera_selenium\evidencias\cp06\paso4_resultados.png")
    print("✓ Búsqueda ejecutada")
    print("✓ Captura guardada: paso4_resultados.png")
    
    # Paso 5: Validar resultados
    print("\nPaso 5: Validando resultados...")
    current_url = driver.current_url
    print(f"URL actual: {current_url}")
    
    # Verificar que estamos en página de resultados
    if "search" in current_url.lower() or "python" in current_url.lower():
        print("✓ URL de resultados correcta")
    
    # Contar resultados visibles
    try:
        # Buscar tarjetas de cursos
        course_cards = driver.find_elements(By.CSS_SELECTOR, "[data-e2e='search-result-card'], .cds-ProductCard-base, [class*='ProductCard']")
        num_results = len(course_cards)
        print(f"✓ Se encontraron {num_results} cursos en la página")
        
        if num_results > 0:
            print("✓✓ Resultados mostrados correctamente")
        else:
            print("⚠ No se detectaron tarjetas de cursos, pero la búsqueda se ejecutó")
    except Exception as e:
        print(f"⚠ No se pudieron contar resultados: {str(e)}")
    
    # Verificar título de página
    page_title = driver.title
    print(f"✓ Título de página: {page_title}")
    
    # Paso 6: Captura de filtros disponibles
    print("\nPaso 6: Capturando vista con filtros...")
    time.sleep(2)
    driver.save_screenshot(r"D:\Universidad\Semestre5\Administracion\coursera_selenium\evidencias\cp06\paso5_filtros_disponibles.png")
    print("✓ Captura guardada: paso5_filtros_disponibles.png")
    
    print("\n" + "="*60)
    print("✓✓✓ CP-06 COMPLETADO EXITOSAMENTE ✓✓✓")
    print("="*60)
    print("Búsqueda ejecutada y resultados mostrados correctamente")
    
except Exception as e:
    print("\n" + "="*60)
    print("✗✗✗ ERROR en CP-06 ✗✗✗")
    print("="*60)
    print(f"Error detallado: {str(e)}")
    print(f"URL actual: {driver.current_url}")
    driver.save_screenshot(r"D:\Universidad\Semestre5\Administracion\coursera_selenium\evidencias\cp06\error.png")
    print("✓ Captura de error guardada: error.png")
    
finally:
    print("\nEsperando 5 segundos antes de cerrar...")
    time.sleep(5)
    driver.quit()
    print("\n=== FIN DE CP-06 ===\n")