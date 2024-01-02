function valid() {
      let username = document.forms["form"]["username"].value;
      let email = document.forms["form"]["email"].value;
      let jam_pemberangkatan = document.forms["form"]["jam_pemberangkatan"];
      let Tujuan_pemberangkatan =
        document.forms["form"]["Tujuan_pemberangkatan"];
      let Jumlah_tiket = document.forms["form"]["Jumlah_tiket"];
      let emailValid =
        /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
      let jamValid = /^([0-1][0-9]|2[0-3]):([0-5][0-9])$/;
      //nama pengguna
      if (username.length > 30) {
        document.getElementById("error1").textContent = "Error";
        document.forms["form"]["username"].value = "";
        document.getElementById("data").innerHTML = "";
        alert("Data tidak valid\nNama melebihi 30 karakter");
      } else if (username == "") {
        document.getElementById("error1").textContent = "Error";
        document.forms["form"]["username"].value = "";
        document.getElementById("data").innerHTML = "";
        alert("Data tidak valid\nNama harus diisi");
        
      } 
      //email
      else if (email == "") {
        document.getElementById("error2").textContent = "Error";
        document.forms["form"]["email"].value = "";
        document.getElementById("data").innerHTML = "";
        alert("Data tidak valid\nEmail harus diisi");
      } 
      else if (!email.match(emailValid)) {
        document.getElementById("error2").textContent = "Error";
        document.forms["form"]["email"].value = "";
        document.getElementById("data").innerHTML = "";
        alert("Data tidak valid\nFormat email tidak sesuai");
      } 
      //jam berangkat
      else if (jam_pemberangkatan == "") {
        document.getElementById("error3").textContent = "Error";
        document.forms["form"]["jam_pemberangkatan"].value = "";
        document.getElementById("data").innerHTML = "";
        alert("Data tidak valid\nJam harus diisi");
      } 
      else if (!jam_pemberangkatan.match(jamValid)) {
        document.getElementById("error3").textContent = "Error";
        document.forms["form"]["jam_pemberangkatan"].value = "";
        document.getElementById("data").innerHTML = "";
        alert("Data tidak valid\nFormat jam tidak sesuai");
      } 
      //tujuan
      else if (Tujuan_pemberangkatan == "") {
        document.getElementById("error4").textContent = "Error";
        document.forms["form"]["Tujuan_pemberangkatan"].value = "";
        document.getElementById("data").innerHTML = "";
        alert("Data tidak valid\nTujuan harus diisi");
      } 
      else if (Jumlah_tiket == "") {
        document.getElementById("error5").textContent = "Error";
        document.forms["form"]["Jumlah_tiket"].value = "";
        document.getElementById("data").innerHTML = "";
        alert("Data tidak valid\nJumlah tiket harus diisi");
      }
      //jumlah tiket
      else if (Jumlah_tiket < 1 || Jumlah_tiket > 10) {
        document.getElementById("error5").textContent = "Error";
        document.forms["form"]["Jumlah_tiket"].value = "";
        document.getElementById("data").innerHTML = "";
        alert("Data tidak valid\nLimit jumlah tiket 1 - 10");
      }
      else{
        document.getElementById("buatdata").innerHTML =
          '<table id="data"><tr><th>Username</th><td><span id="Namapengguna">' +
          username +
          '</span></td></tr><tr><th>Email</th><td><span id="emailpengguna">' +
          email +
          '</span></td></tr><tr><th>Jam Pemberangkatan</th><td><span id="jambernagkat">' +
          jam_pemberangkatan +
          '</span></td></tr> <tr><th>Tujuan Pemberangkatan</th><td><span id="tujuanberangkat">' +
          Tujuan_pemberangkatan +
          '</span></td></tr><tr><th>Jumlah Tiket</th><td><span id="jumlahtiket">' +
          Jumlah_tiket +
          "</span></td></tr>";
        document.getElementById("error1").textContent = "";
        document.getElementById("error2").textContent = "";
        document.getElementById("error3").textContent = "";
        document.getElementById("error4").textContent = "";
        document.getElementById("error5").textContent = "";
      }
    }