from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
  return "<p> Nama : Jamiatul Khasanah </p><p>Tempat,Tanggal Lahir : Malang, 11 Juni 2004</p><p> Alamat : Dusun.Boro Watugede, Singosari, Malang</p><p> Jenis Kelamin : Perempuan</p><p> Kewarganegaraan : Indonesia</p><p>Agama : Islam</p>"


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
