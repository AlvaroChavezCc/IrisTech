const tableHeaderStyle = {
  backgroundColor: "#f2f2f2",
  padding: 8,
  border: "1px solid #ddd",
};

const tableCellStyle = {
  padding: 8,
  border: "1px solid #ddd",
  color: "blue",
};

export default function F12Main() {
  return (
    <div style={{ padding: 20 }}>
      <h1 style={{ marginBottom: 20, fontSize: 20 }}>Page List</h1>
      <table style={{ borderCollapse: "collapse", border: "1px solid #ddd" }}>
        <thead>
          <tr>
            <th style={tableHeaderStyle}>URL</th>
            <th style={tableHeaderStyle}>Page</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td style={tableCellStyle}>
              <a href="/DbAlumno">/DbAlumno</a>
            </td>
            <td style={tableCellStyle}>
              <a href="/DbAlumno">DB Alumno</a>
            </td>
          </tr>
          <tr>
            <td style={tableCellStyle}>
              <a href="/DbPrpofesor">/DbPrpofesor</a>
            </td>
            <td style={tableCellStyle}>
              <a href="/DbPrpofesor">DB Prpofesor</a>
            </td>
          </tr>
          <tr>
            <td style={tableCellStyle}>
              <a href="/DbSuperAdministrador">/DbSuperAdministrador</a>
            </td>
            <td style={tableCellStyle}>
              <a href="/DbSuperAdministrador">DB SuperAdministrador</a>
            </td>
          </tr>
          <tr>
            <td style={tableCellStyle}>
              <a href="/DbSuperAdministrador1">/DbSuperAdministrador1</a>
            </td>
            <td style={tableCellStyle}>
              <a href="/DbSuperAdministrador1">DB SuperAdministrador</a>
            </td>
          </tr>

          <tr>
            <td style={tableCellStyle}>
              <a href="/InicioEe">/InicioEe</a>
            </td>
            <td style={tableCellStyle}>
              <a href="/InicioEe">Inicio EE</a>
            </td>
          </tr>
          <tr>
            <td style={tableCellStyle}>
              <a href="/Login">/Login</a>
            </td>
            <td style={tableCellStyle}>
              <a href="/Login">Login</a>
            </td>
          </tr>

          <tr>
            <td style={tableCellStyle}>
              <a href="/Registrarse">/Registrarse</a>
            </td>
            <td style={tableCellStyle}>
              <a href="/Registrarse">Registrarse</a>
            </td>
          </tr>
          <tr>
            <td style={tableCellStyle}>
              <a href="/RegistroAlumno">/RegistroAlumno</a>
            </td>
            <td style={tableCellStyle}>
              <a href="/RegistroAlumno">Registro Alumno</a>
            </td>
          </tr>
          <tr>
            <td style={tableCellStyle}>
              <a href="/RegistroAlumnoIi">/RegistroAlumnoIi</a>
            </td>
            <td style={tableCellStyle}>
              <a href="/RegistroAlumnoIi">Registro Alumno II</a>
            </td>
          </tr>
          <tr>
            <td style={tableCellStyle}>
              <a href="/RegistroProfesor">/RegistroProfesor</a>
            </td>
            <td style={tableCellStyle}>
              <a href="/RegistroProfesor">Registro Profesor</a>
            </td>
          </tr>
          <tr>
            <td style={tableCellStyle}>
              <a href="/RegistroProfesorIi">/RegistroProfesorIi</a>
            </td>
            <td style={tableCellStyle}>
              <a href="/RegistroProfesorIi">Registro Profesor II</a>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  );
}
