from flask import Flask, render_template, request

app = Flask(__name__)

@app.route ('/')
def home():
    return render_template('index.html')

@app.route('/ejercicio1')
def ejercicio():
    return render_template('ejercicio1.html')

@app.route('/Solucion', methods = ['POST'])
def Solucion():
        if request.method == 'POST':
            A = int (request.form['A'])
            B = int (request.form['B'])
            C = int (request.form['C'])
            if A != B and A != C and B != C:
                if A > B and A > C:
                    return render_template('ejercicio1.html', Resultado= 'El Mayor es A', A=A, B=B, C=C)
                elif B > A and B > C:
                    return render_template('ejercicio1.html', Resultado= 'El Mayor es B', A=A, B=B, C=C)
                elif C > A and C > B:
                    return render_template('ejercicio1.html', Resultado= 'El Mayor es C', A=A, B=B, C=C)
                else:
                    return render_template('ejercicio1.html', Resultado= 'Los Numeros Ingresados Deben Ser Diferentes', A=A, B=B, C=C)
                
@app.route('/ejercicio2')
def ejercicio2():
    return render_template('ejercicio2.html')

@app.route('/notas', methods = ['POST'])
def notas():
    if request.method == 'POST':
        nota = int (request.form['nota1'])
        if nota >= 1 and nota <= 9:
            mensaje= "E"
        elif nota >= 10 and nota <= 13:
            mensaje= "D"
        elif nota >= 13 and nota <= 16:
            mensaje= "C"
        elif nota >= 16 and nota <= 19:
            mensaje= "B"
        elif nota >= 19 and nota <= 20:
            mensaje= "A"
        return render_template('ejercicio2.html', resultado=mensaje)
    
@app.route('/ejercicio3')
def ejercicio3():
    return render_template('ejercicio3.html')

@app.route('/Precios', methods = ['POST'])
def Precios():
    if request.method == 'POST':
        Dolar = 1 * 4054
        Precio1 = float (request.form['Precio1'])
        Precio2 = float (request.form['Precio2'])
        Precio3 = float (request.form['Precio3'])
        Precio4 = float (request.form['Precio4'])
        Precio5 = float (request.form['Precio5'])
        suma = Precio1 + Precio2 + Precio3 + Precio4 + Precio5
        Resultado = suma * Dolar
        return render_template('ejercicio3.html', Conversion = Resultado)
    
@app.route('/ejercicio4')
def ejercicio4():
    return render_template('ejercicio4.html')

@app.route('/Desarrollo', methods = ['POST'])
def Desarrollo():
    if request.method == 'POST':
        A = int (request.form['n1'])
        Doble = A * 2 
        Triple = A * 3
        return render_template('ejercicio4.html', A = A, Dob = Doble, Trip = Triple)

@app.route('/ejercicio5', methods=['GET', 'POST'])
def ejercicio5():
    figura = None
    Resultado_area = None
    if request.method == 'POST':
        figura = request.form['figura']
        try:
            if figura == 'circulo':
                radio = float(request.form['radio'])
                Resultado_area = 3.14159 * (radio ** 2)
            elif figura == 'cuadrado':
                lado = float(request.form['lado'])
                Resultado_area = lado ** 2
            elif figura == 'rectangulo':
                largo = float(request.form['largo'])
                ancho = float(request.form['ancho'])
                Resultado_area = largo * ancho
            elif figura == 'triangulo':
                base = float(request.form['base'])
                altura = float(request.form['altura'])
                Resultado_area = 0.5 * base * altura
            else:
                return render_template('ejercicio5.html', error="Figura no válida.")
        except ValueError:
            return render_template('ejercicio5.html', error="Por favor, ingrese valores válidos.")

    return render_template('ejercicio5.html', figura = figura, area = Resultado_area)
    

if __name__ == '__main__':
    app.run()