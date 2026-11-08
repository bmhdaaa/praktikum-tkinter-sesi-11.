import tkinter as tk
from tkinter import ttk, messagebox


class PendaftaranMahasiswa:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Pendaftaran Kegiatan Mahasiswa")
        self.root.geometry("780x720")
        self.root.minsize(700, 650)
        self.root.configure(bg="#f2f5f9")

        self.nama_var = tk.StringVar()
        self.prodi_var = tk.StringVar()
        self.gender_var = tk.StringVar(value="")
        self.kegiatan_vars = {
            "Seminar Teknologi": tk.BooleanVar(),
            "Pelatihan Pemrograman": tk.BooleanVar(),
            "Lomba IT": tk.BooleanVar(),
            "Pengabdian Masyarakat": tk.BooleanVar()
        }

        self.buat_menu()
        self.buat_tampilan()
        self.root.bind("<Return>", self.submit_event)

    def buat_menu(self):
        menu_bar = tk.Menu(self.root)

        menu_file = tk.Menu(menu_bar, tearoff=0)
        menu_file.add_command(label="Keluar", command=self.keluar)
        menu_bar.add_cascade(label="File", menu=menu_file)

        menu_bantuan = tk.Menu(menu_bar, tearoff=0)
        menu_bantuan.add_command(label="About", command=self.tampilkan_about)
        menu_bar.add_cascade(label="Bantuan", menu=menu_bantuan)

        self.root.config(menu=menu_bar)

    def buat_tampilan(self):
        header = tk.Frame(self.root, bg="#173b67", pady=18)
        header.pack(fill="x")

        tk.Label(
            header,
            text="PENDAFTARAN KEGIATAN MAHASISWA",
            font=("Arial", 18, "bold"),
            fg="white",
            bg="#173b67"
        ).pack()

        tk.Label(
            header,
            text="Silakan isi formulir pendaftaran di bawah ini",
            font=("Arial", 10),
            fg="#dce8f5",
            bg="#173b67"
        ).pack(pady=(5, 0))

        container = tk.Frame(self.root, bg="#f2f5f9", padx=22, pady=15)
        container.pack(fill="both", expand=True)

        # Frame formulir
        form = tk.LabelFrame(
            container, text="Formulir Pendaftaran",
            font=("Arial", 11, "bold"), bg="white",
            padx=15, pady=12
        )
        form.pack(fill="x", pady=(0, 12))
        form.columnconfigure(1, weight=1)

        tk.Label(form, text="Nama Lengkap", bg="white").grid(
            row=0, column=0, sticky="w", padx=5, pady=7
        )
        self.nama_entry = ttk.Entry(form, textvariable=self.nama_var)
        self.nama_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=7)

        tk.Label(form, text="Program Studi", bg="white").grid(
            row=1, column=0, sticky="w", padx=5, pady=7
        )
        prodi = ttk.Combobox(
            form,
            textvariable=self.prodi_var,
            values=[
                "Teknik Informatika",
                "Sistem Informasi",
                "Manajemen",
                "Akuntansi",
                "Teknik Sipil"
            ],
            state="readonly"
        )
        prodi.grid(row=1, column=1, sticky="ew", padx=5, pady=7)
        prodi.set("Pilih Program Studi")

        tk.Label(form, text="Jenis Kelamin", bg="white").grid(
            row=2, column=0, sticky="nw", padx=5, pady=7
        )
        gender_frame = tk.Frame(form, bg="white")
        gender_frame.grid(row=2, column=1, sticky="w", padx=5, pady=7)
        tk.Radiobutton(
            gender_frame, text="Laki-laki", variable=self.gender_var,
            value="Laki-laki", bg="white"
        ).pack(side="left", padx=(0, 15))
        tk.Radiobutton(
            gender_frame, text="Perempuan", variable=self.gender_var,
            value="Perempuan", bg="white"
        ).pack(side="left")

        tk.Label(form, text="Pilih Kegiatan", bg="white").grid(
            row=3, column=0, sticky="nw", padx=5, pady=7
        )
        kegiatan_frame = tk.Frame(form, bg="white")
        kegiatan_frame.grid(row=3, column=1, sticky="w", padx=5, pady=7)

        for index, (nama, variable) in enumerate(self.kegiatan_vars.items()):
            tk.Checkbutton(
                kegiatan_frame, text=nama, variable=variable, bg="white"
            ).grid(row=index // 2, column=index % 2, sticky="w", padx=(0, 18), pady=2)

        tk.Label(form, text="Alasan Mengikuti", bg="white").grid(
            row=4, column=0, sticky="nw", padx=5, pady=7
        )
        self.alasan_text = tk.Text(form, height=4, wrap="word", font=("Arial", 10))
        self.alasan_text.grid(row=4, column=1, sticky="ew", padx=5, pady=7)

        # Listbox pilihan kegiatan
        list_frame = tk.LabelFrame(
            container, text="Daftar Pilihan Kegiatan",
            font=("Arial", 10, "bold"), bg="white",
            padx=12, pady=8
        )
        list_frame.pack(fill="x", pady=(0, 12))

        self.listbox = tk.Listbox(list_frame, height=4, font=("Arial", 10))
        daftar = [
            "Seminar Teknologi",
            "Pelatihan Pemrograman",
            "Lomba IT",
            "Pengabdian Masyarakat"
        ]
        for item in daftar:
            self.listbox.insert(tk.END, item)
        self.listbox.pack(fill="x")

        # Tombol aksi
        tombol_frame = tk.Frame(container, bg="#f2f5f9")
        tombol_frame.pack(fill="x", pady=(0, 12))

        ttk.Button(
            tombol_frame, text="Submit / Daftar",
            command=self.submit
        ).pack(side="left", padx=(0, 8))

        ttk.Button(
            tombol_frame, text="Reset",
            command=self.reset
        ).pack(side="left")

        # Area informasi
        info_frame = tk.LabelFrame(
            container, text="Informasi Pendaftaran",
            font=("Arial", 10, "bold"), bg="white",
            padx=12, pady=8
        )
        info_frame.pack(fill="both", expand=True)

        self.hasil_text = tk.Text(
            info_frame, height=7, wrap="word",
            font=("Arial", 10), state="disabled",
            bg="#f8fafc"
        )
        self.hasil_text.pack(fill="both", expand=True)

        tk.Label(
            self.root,
            text="Praktikum Python Tkinter | Sesi 11",
            bg="#f2f5f9", fg="#667085",
            font=("Arial", 9)
        ).pack(pady=(0, 8))

        self.nama_entry.focus_set()

    def submit_event(self, event):
        self.submit()

    def submit(self):
        nama = self.nama_var.get().strip()
        prodi = self.prodi_var.get()
        gender = self.gender_var.get()
        alasan = self.alasan_text.get("1.0", tk.END).strip()

        kegiatan = [
            nama_kegiatan
            for nama_kegiatan, variable in self.kegiatan_vars.items()
            if variable.get()
        ]

        # Validasi input
        if not nama:
            messagebox.showwarning("Peringatan", "Nama tidak boleh kosong!")
            self.nama_entry.focus_set()
            return

        if not prodi or prodi == "Pilih Program Studi":
            messagebox.showwarning("Peringatan", "Silakan pilih program studi!")
            return

        if not gender:
            messagebox.showwarning("Peringatan", "Silakan pilih jenis kelamin!")
            return

        if not kegiatan:
            messagebox.showwarning("Peringatan", "Pilih minimal satu kegiatan!")
            return

        # Menampilkan ringkasan pendaftaran
        ringkasan = (
            "PENDAFTARAN BERHASIL\n"
            "====================================\n"
            f"Nama           : {nama}\n"
            f"Program Studi  : {prodi}\n"
            f"Jenis Kelamin  : {gender}\n"
            "Kegiatan       :\n"
        )
        for nomor, item in enumerate(kegiatan, start=1):
            ringkasan += f"  {nomor}. {item}\n"

        ringkasan += (
            f"Alasan         : {alasan if alasan else '-'}\n"
            "====================================\n"
            "Terima kasih telah melakukan pendaftaran."
        )

        self.hasil_text.config(state="normal")
        self.hasil_text.delete("1.0", tk.END)
        self.hasil_text.insert(tk.END, ringkasan)
        self.hasil_text.config(state="disabled")

        messagebox.showinfo(
            "Pendaftaran Berhasil",
            f"Terima kasih, {nama}!\nData pendaftaran berhasil diproses."
        )

    def reset(self):
        self.nama_var.set("")
        self.prodi_var.set("Pilih Program Studi")
        self.gender_var.set("")

        for variable in self.kegiatan_vars.values():
            variable.set(False)

        self.alasan_text.delete("1.0", tk.END)
        self.listbox.selection_clear(0, tk.END)

        self.hasil_text.config(state="normal")
        self.hasil_text.delete("1.0", tk.END)
        self.hasil_text.config(state="disabled")

        self.nama_entry.focus_set()

    def tampilkan_about(self):
        about = tk.Toplevel(self.root)
        about.title("About Aplikasi")
        about.geometry("370x230")
        about.resizable(False, False)
        about.transient(self.root)

        tk.Label(
            about,
            text="PENDAFTARAN KEGIATAN MAHASISWA",
            font=("Arial", 12, "bold"),
            fg="#173b67"
        ).pack(pady=(25, 12))

        tk.Label(
            about,
            text=(
                "Aplikasi ini dibuat menggunakan Python Tkinter.\n\n"
                "Tujuan: mempermudah proses pendaftaran kegiatan\n"
                "mahasiswa melalui antarmuka GUI.\n\n"
                "Praktikum Sesi 11 - Advanced Widgets\n"
                "dan Event Handling"
            ),
            justify="center",
            font=("Arial", 9)
        ).pack(padx=15)

        ttk.Button(about, text="Tutup", command=about.destroy).pack(pady=15)

    def keluar(self):
        if messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin keluar?"):
            self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = PendaftaranMahasiswa(root)
    root.mainloop()
