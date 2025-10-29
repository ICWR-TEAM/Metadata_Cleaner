import os
from PIL import Image

class Main:
    def remove_metadata(self, input_path, output_dir=None, suffix="_cleaned"):
        ########################################################################
        # Menghapus metadata dari gambar dan menyimpan versi bersihnya.        #
        ########################################################################
        try:
            image = Image.open(input_path)
            data = list(image.getdata())
            clean_image = Image.new(image.mode, image.size)
            clean_image.putdata(data)

            filename = os.path.basename(input_path)
            name, ext = os.path.splitext(filename)

            output_filename = f"{name}{suffix}{ext}"

            if output_dir:
                os.makedirs(output_dir, exist_ok=True)
                output_path = os.path.join(output_dir, output_filename)
            else:
                output_path = os.path.join(os.path.dirname(input_path), output_filename)

            clean_image.save(output_path)
            print(f"✅ {filename} dibersihkan → {output_path}")
            return output_path

        except Exception as e:
            print(f"❌ Gagal membersihkan {input_path}: {e}")
            return None

    def clean_folder(self, folder_path, output_dir=None, suffix="_cleaned"):
        #########################################################
        # Membersihkan metadata dari semua gambar dalam folder. #
        #########################################################
        supported = (".jpg", ".jpeg", ".png", ".tiff", ".bmp", ".webp")
        files = [f for f in os.listdir(folder_path) if f.lower().endswith(supported)]

        if not files:
            print("⚠️ Tidak ada gambar yang ditemukan di folder ini.")
            return

        for file in files:
            file_path = os.path.join(folder_path, file)
            self.remove_metadata(file_path, output_dir=output_dir, suffix=suffix)

if __name__ == "__main__":
    cleaner = Main()

    print("==========================")
    print("# Image Metadata Cleaner #")
    print("==========================")
    print("Masukkan path file atau folder gambar:")

    target = input("📂 > ").strip()

    print("Masukkan direktori output (kosongkan jika ingin simpan di folder asal):")
    output_dir = input("📁 > ").strip() or None

    print("Masukkan suffix untuk nama file output (default: _cleaned):")
    suffix = input("🔤 > ").strip() or "_cleaned"

    if os.path.isfile(target):
        cleaner.remove_metadata(target, output_dir=output_dir, suffix=suffix)
    elif os.path.isdir(target):
        cleaner.clean_folder(target, output_dir=output_dir, suffix=suffix)
    else:
        print("❌ Path tidak valid. Pastikan path file atau folder benar.")
