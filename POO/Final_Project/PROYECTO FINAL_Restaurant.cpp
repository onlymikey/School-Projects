#include <iostream>
#include <vector>
#include <string>
using namespace std;

// Clase Producto
class Producto {
public:
    string nombre;
    double precio;
    int existencias;
    Producto(string nombre, double precio, int existencias) : nombre(nombre), precio(precio), existencias(existencias) {}
};

// Clase Cliente
class Cliente {
public:
    string nombre;
    vector<Producto> carrito;
    Cliente(string nombre) : nombre(nombre) {}
    void agregarProductoAlCarrito(Producto producto) {
        carrito.push_back(producto);
    }
    void mostrarCarrito() {
        cout << "Carrito de " << nombre << ":\n";
        for (Producto p : carrito) {
            cout << "- " << p.nombre << ": $" << p.precio << endl;
        }
    }
};

// Clase Pedido
class Pedido {
public:
    Cliente cliente;
    vector<Producto> productos;
    double total;
    Pedido(Cliente cliente) : cliente(cliente), total(0) {}
    void calcularTotal() {
        total = 0;
        for (Producto p : productos) {
            total += p.precio;
        }
    }
    void mostrarPedido() {
        cout << "Pedido de " << cliente.nombre << ":\n";
        for (Producto p : productos) {
            cout << "- " << p.nombre << ": $" << p.precio << endl;
        }
        cout << "Total: $" << total << endl;
    }
    int contarProducto(string nombreProducto) {
        int count = 0;
        for (Producto p : productos) {
            if (p.nombre == nombreProducto) {
                count++;
            }
        }
        return count;
    }
    void eliminarProducto(string nombreProducto, int cantidad) {
        int count = 0;
        for (auto it = productos.begin(); it != productos.end() && count < cantidad;) {
            if (it->nombre == nombreProducto) {
                it = productos.erase(it);
                count++;
            } else {
                ++it;
            }
        }
        calcularTotal();
    }
};

// Clase SistemaDeGestion
class SistemaDeGestion {
public:
    vector<Producto> menu;
    vector<Pedido> pedidos;
    void agregarProductoAlMenu(string nombre, double precio, int existencias) {
        menu.push_back(Producto(nombre, precio, existencias));
    }
    void mostrarMenu() {
        cout << "\n--- Menu del Restaurante ---\n";
        for (size_t i = 0; i < menu.size(); ++i) {
            cout << i + 1 << ". " << menu[i].nombre << ": $" << menu[i].precio << " (Existencias: " << menu[i].existencias << ")\n";
        }
        cout << "----------------------------\n";
    }
    void crearPedido(Cliente cliente) {
        Pedido nuevoPedido(cliente);
        pedidos.push_back(nuevoPedido);
    }
    void agregarProductoAPedido(int pedidoIndex, int productoIndex, int cantidad) {
        Producto& producto = menu[productoIndex];
        if (producto.existencias >= cantidad) {
            for (int i = 0; i < cantidad; ++i) {
                pedidos[pedidoIndex].productos.push_back(producto);
            }
            pedidos[pedidoIndex].calcularTotal();
            producto.existencias -= cantidad;
        } else {
            cout << "Producto sin existencias suficientes.\n";
        }
    }
    void eliminarProductoDePedido(int pedidoIndex, int productoIndex, int cantidad) {
        Producto& producto = menu[productoIndex];
        int cantidadEnPedido = pedidos[pedidoIndex].contarProducto(producto.nombre);
        if (cantidad > cantidadEnPedido) {
            cantidad = cantidadEnPedido;
        }
        pedidos[pedidoIndex].eliminarProducto(producto.nombre, cantidad);
        producto.existencias += cantidad;
    }
    void mostrarPedidos() {
        cout << "\n--- Pedidos ---\n";
        for (size_t i = 0; i < pedidos.size(); ++i) {
            cout << i + 1 << ". ";
            pedidos[i].mostrarPedido();
        }
        cout << "----------------\n";
    }
    void modificarPedido(int pedidoIndex, int productoIndex, string accion, int cantidad = 1) {
        if (accion == "agregar") {
            agregarProductoAPedido(pedidoIndex, productoIndex, cantidad);
        } else if (accion == "eliminar") {
            eliminarProductoDePedido(pedidoIndex, productoIndex, cantidad);
        }
    }
    void modificarExistencias(int productoIndex, int nuevasExistencias) {
        if (productoIndex >= 0 && productoIndex < menu.size()) {
            menu[productoIndex].existencias = nuevasExistencias;
            cout << "Existencias de " << menu[productoIndex].nombre << " actualizadas a " << nuevasExistencias << ".\n";
        } else {
            cout << "Índice de producto no válido.\n";
        }
    }
};

// Main
int main() {
    SistemaDeGestion sistema;

    // Agregar productos al menú
    sistema.agregarProductoAlMenu("Hamburguesa", 50.0, 10);
    sistema.agregarProductoAlMenu("Papas Fritas", 25.0, 20);
    sistema.agregarProductoAlMenu("Refresco", 15.0, 30);

    // Menú interactivo
    int opcion;
    do {
        cout << "\n****************************\n";
        cout << "1. Mostrar menú\n";
        cout << "2. Crear pedido\n";
        cout << "3. Modificar pedido\n";
        cout << "4. Mostrar pedidos\n";
        cout << "5. Modificar inventario\n";
        cout << "6. Salir\n";
        cout << "****************************\n";
        cout << "Seleccione una opción: ";
        cin >> opcion;

        switch (opcion) {
            case 1:
                sistema.mostrarMenu();
                break;
            case 2: {
                cout << "\n--- Crear Pedido ---\n";
                string nombreCliente;
                cout << "Ingrese el nombre del cliente: ";
                cin >> nombreCliente;
                Cliente cliente(nombreCliente);
                sistema.crearPedido(cliente);

                int pedidoIndex = sistema.pedidos.size() - 1;
                int productoIndex, cantidad;
                do {
                    sistema.mostrarMenu();
                    cout << "Ingrese el índice del producto a agregar (0 para terminar): ";
                    cin >> productoIndex;
                    if (productoIndex > 0 && productoIndex <= sistema.menu.size()) {
                        cout << "Ingrese la cantidad: ";
                        cin >> cantidad;
                        sistema.agregarProductoAPedido(pedidoIndex, productoIndex - 1, cantidad);
                    } else if (productoIndex != 0) {
                        cout << "Índice de producto no válido.\n";
                    }
                } while (productoIndex != 0);
                cout << "----------------------\n";
                break;
            }
            case 3: {
                cout << "\n--- Modificar Pedido ---\n";
                int pedidoIndex;
                cout << "Ingrese el índice del pedido: ";
                cin >> pedidoIndex;
                if (pedidoIndex > 0 && pedidoIndex <= sistema.pedidos.size()) {
                    int productoIndex, cantidad;
                    string accion;
                    int accionNum;
                    do {
                        sistema.mostrarMenu();
                        cout << "Ingrese el índice del producto: ";
                        cin >> productoIndex;
                        if (productoIndex > 0 && productoIndex <= sistema.menu.size()) {
                            cout << "Ingrese la acción (1. agregar / 2. eliminar): ";
                            cin >> accionNum;
                            if (accionNum == 1) {
                                accion = "agregar";
                                cout << "Ingrese la cantidad: ";
                                cin >> cantidad;
                                sistema.modificarPedido(pedidoIndex - 1, productoIndex - 1, accion, cantidad);
                            } else if (accionNum == 2) {
                                accion = "eliminar";
                                cout << "Ingrese la cantidad: ";
                                cin >> cantidad;
                                sistema.modificarPedido(pedidoIndex - 1, productoIndex - 1, accion, cantidad);
                            } else {
                                cout << "Acción no válida.\n";
                            }
                        } else {
                            cout << "Índice de producto no válido.\n";
                        }
                        cout << "¿Desea modificar algo más en este pedido? (1. Sí / 0. No): ";
                        cin >> accionNum;
                    } while (accionNum == 1);
                } else {
                    cout << "Índice de pedido no válido.\n";
                }
                cout << "-------------------------\n";
                break;
            }
            case 4:
                sistema.mostrarPedidos();
                break;
            case 5: {
                cout << "\n--- Modificar Inventario ---\n";
                int subOpcion;
                cout << "1. Agregar nuevo producto\n";
                cout << "2. Modificar existencias de producto\n";
                cout << "Seleccione una opción: ";
                cin >> subOpcion;
                if (subOpcion == 1) {
                    string nombre;
                    double precio;
                    int existencias;
                    cout << "Ingrese el nombre del producto: ";
                    cin >> nombre;
                    cout << "Ingrese el precio del producto: ";
                    cin >> precio;
                    cout << "Ingrese las existencias del producto: ";
                    cin >> existencias;
                    sistema.agregarProductoAlMenu(nombre, precio, existencias);
                    cout << "Producto agregado al menú.\n";
                } else if (subOpcion == 2) {
                    int productoIndex, nuevasExistencias;
                    sistema.mostrarMenu();
                    cout << "Ingrese el índice del producto: ";
                    cin >> productoIndex;
                    cout << "Ingrese las nuevas existencias: ";
                    cin >> nuevasExistencias;
                    sistema.modificarExistencias(productoIndex - 1, nuevasExistencias);
                } else {
                    cout << "Opción no válida.\n";
                }
                cout << "-------------------------\n";
                break;
            }
            case 6:
                cout << "Saliendo...\n";
                break;
            default:
                cout << "Opción no válida.\n";
                break;
        }
    } while (opcion != 6);

    return 0;
}