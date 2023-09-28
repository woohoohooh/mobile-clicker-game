import os
import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import AsyncImage
from kivy.uix.label import Label
from kivy.clock import Clock

class HBoxLayoutExample(App):
    def build(self):
        self.image_dir = 'img'
        self.mob_hp_images = self.get_image_files(self.image_dir)
        self.mob_hp_index = 0
        layout = BoxLayout(padding=10, spacing=10, orientation='vertical')

        self.img2_area_x = 0
        self.img2_area_y = 0
        self.img2_area_width = 1000
        self.img2_area_height = 1000

        self.mob_image = AsyncImage(source=self.get_next_image(), size_hint=(None, None), size=(800, 800))
        self.mob_image.bind(on_touch_down=self.on_image_click)
        layout.add_widget(self.mob_image)

        self.hero_level = 1
        self.hero_level_label = Label(text=f'Уровень: {self.hero_level}')
        layout.add_widget(self.hero_level_label)

        self.img2_counter = 0
        self.overlay_images = []

        return layout

    def on_image_click(self, instance, touch):
        if (self.img2_area_x < touch.x < self.img2_area_x + self.img2_area_width and
                self.img2_area_y < touch.y < self.img2_area_y + self.img2_area_height):
            self.img2_counter += 1

            if self.img2_counter == 3:
                self.remove_overlay_images()
                self.mob_hp_index = (self.mob_hp_index + 1) % len(self.mob_hp_images)
                Clock.schedule_once(self.update_main_image, 0.5)
                self.img2_counter = 0

            img2_files = self.get_image_files('img2')
            if img2_files:
                random_image = random.choice(img2_files)
                random_image_path = os.path.join('img2', random_image)
                if os.path.exists(random_image_path):
                    random_async_image = AsyncImage(source=random_image_path, size_hint=(None, None), size=(200, 200))
                    random_async_image.center = (touch.x, touch.y)
                    instance.add_widget(random_async_image)
                    self.overlay_images.append(random_async_image)

                    # Запускаем таймер на 1 секунду для удаления изображения
                    Clock.schedule_once(lambda dt, image=random_async_image: self.remove_overlay_image(image), 0.1)

        else:
            self.hero_level += 1
            self.hero_level_label.text = f'Уровень: {self.hero_level}'

    def remove_overlay_images(self):
        for image in self.overlay_images:
            if image.parent is not None:
                image.parent.remove_widget(image)
        self.overlay_images = []

    def remove_overlay_image(self, image):
        if image in self.overlay_images and image.parent is not None:
            image.parent.remove_widget(image)
            self.overlay_images.remove(image)

    def update_main_image(self, dt):
        self.mob_image.source = self.get_next_image()

    def get_image_files(self, directory):
        image_files = [f for f in os.listdir(directory) if f.endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
        return image_files

    def get_next_image(self):
        if self.mob_hp_index < len(self.mob_hp_images):
            image_path = os.path.join(self.image_dir, self.mob_hp_images[self.mob_hp_index])
            if os.path.exists(image_path):
                return image_path
            else:
                # Обработка ошибки, если изображение не найдено
                print(f"Image not found: {image_path}")
        else:
            print("No more images to display.")
        return ''

if __name__ == '__main__':
    app = HBoxLayoutExample()
    app.run()
