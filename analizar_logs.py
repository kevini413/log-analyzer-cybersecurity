def analizar_log(file_path):
    with open(file_path, 'r') as archivo:
        lineas = archivo.readlines()

    resumen = {
        "login_failures": 0,
        "login_successes": 0,
        "sql_injections": 0,
        "suspicious_uploads": 0
    }

    for linea in lineas:
        if "LOGIN FAILED" in linea:
            resumen["login_failures"] += 1
        elif "LOGIN SUCCESS" in linea:
            resumen["login_successes"] += 1
        elif "SQL INJECTION" in linea:
            resumen["sql_injections"] += 1
        elif "UPLOADED" in linea:
            resumen["suspicious_uploads"] += 1

    return resumen

def generar_reporte_simulado(resumen):
    return f"""\
Incident Summary:

The system recorded {resumen['login_failures']} failed login attempt(s), indicating possible brute-force activity. 
There were {resumen['login_successes']} successful login(s), which appear normal.

Detected {resumen['sql_injections']} SQL injection attempt(s), suggesting a direct attack on the application's database.

Additionally, there were {resumen['suspicious_uploads']} suspicious file upload(s), which could be a sign of remote shell injection.

Recommendations:
- Block repeated failed login IPs temporarily.
- Review database firewall rules.
- Inspect uploaded files for backdoors.
- Enable multi-factor authentication (MFA) for all accounts.

End of report.
"""

def guardar_reporte(texto):
    with open("report.txt", "w") as f:
        f.write(texto)
    print("✅ Report generated successfully: report.txt")

if __name__ == "__main__":
    datos = analizar_log("log.txt")
    texto = generar_reporte_simulado(datos)
    guardar_reporte(texto)
