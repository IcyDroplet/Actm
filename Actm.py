import os
from PIL import Image
import colorsys

# Input / output directories
INPUT_DIR = r"C:\Users\IcyDroplet\Desktop\precolorized items"
OUTPUT_DIR = r"C:\Users\IcyDroplet\Desktop\recolorized items"

VARIANT_HUE_MAP = {
    "wool_colored_white": 330,
    "wool_colored_orange": 345,
    "wool_colored_magenta": 320,
    "wool_colored_light_blue": 335,
    "wool_colored_yellow": 340,
    "wool_colored_lime": 325,
    "wool_colored_pink": 330,
    "wool_colored_gray": 315,
    "wool_colored_silver": 330,
    "wool_colored_cyan": 310,
    "wool_colored_purple": 325,
    "wool_colored_blue": 320,
    "wool_colored_brown": 300,
    "wool_colored_green": 305,
    "wool_colored_red": 340,
    "wool_colored_black": 310,

    "hardened_clay_stained_white": 330,
    "hardened_clay_stained_orange": 345,
    "hardened_clay_stained_magenta": 320,
    "hardened_clay_stained_light_blue": 335,
    "hardened_clay_stained_yellow": 340,
    "hardened_clay_stained_lime": 325,
    "hardened_clay_stained_pink": 330,
    "hardened_clay_stained_gray": 315,
    "hardened_clay_stained_silver": 330,
    "hardened_clay_stained_cyan": 310,
    "hardened_clay_stained_purple": 325,
    "hardened_clay_stained_blue": 320,
    "hardened_clay_stained_brown": 300,
    "hardened_clay_stained_green": 305,
    "hardened_clay_stained_red": 340,
    "hardened_clay_stained_black": 310,
    "hardened_clay": 300,

    "glass_white": 330,
    "glass_orange": 345,
    "glass_magenta": 320,
    "glass_light_blue": 335,
    "glass_yellow": 340,
    "glass_lime": 325,
    "glass_pink": 330,
    "glass_gray": 315,
    "glass_silver": 330,
    "glass_cyan": 310,
    "glass_purple": 325,
    "glass_blue": 320,
    "glass_brown": 300,
    "glass_green": 305,
    "glass_red": 340,
    "glass_black": 310,

    "glass_pane_top_white": 330,
    "glass_pane_top_orange": 345,
    "glass_pane_top_magenta": 320,
    "glass_pane_top_light_blue": 335,
    "glass_pane_top_yellow": 340,
    "glass_pane_top_lime": 325,
    "glass_pane_top_pink": 330,
    "glass_pane_top_gray": 315,
    "glass_pane_top_silver": 330,
    "glass_pane_top_cyan": 310,
    "glass_pane_top_purple": 325,
    "glass_pane_top_blue": 320,
    "glass_pane_top_brown": 300,
    "glass_pane_top_green": 305,
    "glass_pane_top_red": 340,
    "glass_pane_top_black": 310,

    "planks_oak": 330,
    "planks_spruce": 335,
    "planks_birch": 325,
    "planks_jungle": 340,
    "planks_acacia": 345,
    "planks_big_oak": 310,

    "leaves_oak": 330,
    "leaves_spruce": 335,
    "leaves_birch": 325,
    "leaves_jungle": 340,
    "leaves_acacia": 345,
    "leaves_big_oak": 310,

    "sapling_oak": 330,
    "sapling_spruce ": 335,
    "sapling_birch": 325,
    "sapling_jungle": 340,
    "sapling_acacia": 345,
    "sapling_roofed_oak": 310,

}
ITEM_HUE_MAP = {
        "glowstone": 325,
        "sandstone_slab": 330,
        "sandstone_slab_top": 330,
        "sandstone_normal": 330,
        "sandstone_bottom": 330,
        "sandstone_top": 330,
        "sandstone_carved": 330,
        "red_sandstone_normal": 335,
        "red_sandstone_bottom": 335,
        "red_sandstone_top": 335,
        "red_sandstone_slab": 335,
        "red_sandstone_slab_top": 335,
        "sandstone_stairs": 330,
        "red_sandstone_stairs": 335,
        "sandstone_chiseled": 325,
        "red_sandstone_chiseled": 330,
        "sandstone_smooth": 335,
        "red_sandstone_smooth": 340,
        "granite": 340,
        "granite_smooth": 335,
        "nether_brick": 320,
        "nether_brick_slab": 320,
        "nether_brick_slab_top": 320,
        "nether_brick_stairs": 320,
        "nether_brick_fence": 320,
        "end_stone": 330,
        "sand": 340,
        "ender_pearl": 340,
        "torch": 340,
        "torch_on": 340,
        "redstone_torch_off": 340,
        "redstone_torch_on": 340,
        "red_sand": 340,
        "obsidian": 300,
        "end_portal_frame": 320,
        "end_portal_frame_top": 320,
        "slime_block": 330,
        "quartz_block": 345,
        "quartz_chiseled": 345,
        "quartz_pillar": 345,
        "cauldron": 325,
        "cauldron_water": 330,
        "cauldron_lava": 340,
        "anvil": 310,
        "hopper": 315,
        "diamond_sword": 330,
        "diamond_pickaxe": 330,
        "diamond_helmet": 330,
        "diamond_chestplate": 330,
        "diamond_leggings": 330,
        "diamond_boots": 330,
        "diamond_horse_armor": 330,
        "golden_apple": 340,
        "gold_ingot": 340,
        "gold_sword": 340,
        "gold_pickaxe": 340,
        "gold_helmet": 340,
        "sandstone": 340,
        "sandstone_smooth": 335,
        "sandstone_chiseled": 325,
        "sandstone_cut": 330,
        "sandstone_slab": 330,
        "sandstone_slab_top": 330,
        "red_sandstone": 340,
        "red_sandstone_smooth": 340,
        "red_sandstone_chiseled": 340,
        "red_sandstone_cut": 340,
        "red_sandstone_slab": 340,
        "red_sandstone_slab_top": 340,
        "obsidian": 300,
        "end_stone": 330,
        "end_portal_frame": 320,
        "end_portal_frame_top": 320,
        "slime_block": 330,
        "quartz_block": 345,
        "quartz_chiseled": 345,
        "quartz_pillar": 345,
        "cauldron": 325,
        "cauldron_water": 330,
        "cauldron_lava": 340,
        "cauldron_powder_snow": 330,
        "anvil": 310,
        "anvil_damaged_1": 310,
        "anvil_damaged_2": 310,
        "anvil_damaged_3": 310,
        "hopper": 315,
        "hopper_locked": 315,
        "fire_layer_0": 320,
        "fire_layer_1": 320,
        "granite": 340,
        "granite_smooth": 335,
        "granite_slab": 340,
        "granite_slab_top": 340,
        "granite_stairs": 340,
        "granite_wall": 340,
        "granite_pressure_plate": 340,
        "granite_button": 340,
        "nether_brick": 320,
        "nether_brick_slab": 320,
        "nether_brick_slab_top": 320,
        "nether_brick_stairs": 320,
        "nether_brick_wall": 320,
        "nether_brick_fence": 320,
        "nether_brick_pressure_plate": 320,
        "nether_brick_button": 320,
        "red_nether_brick": 320,
        "red_nether_brick_slab": 320,
        "red_nether_brick_slab_top": 320,
        "red_nether_brick_stairs": 320,
        "red_nether_brick_wall": 320,
        "red_nether_brick_fence": 320,
        "red_nether_brick_pressure_plate": 320,
        "red_nether_brick_button": 320,
        "chiseled_nether_brick": 320,
        "cracked_nether_brick": 320,
        "cobblestone": 330,
        "stone_brick": 330,
        "stone": 330,
        "bow_standby": 330,
        "andesite": 330,
        "clay": 330,
        "bow_pulling_0": 335,
        "bow_pulling_1": 340,
        "bow_pulling_2": 345,
        "endframe_top": 320,
        "endframe_side": 320,
        "diamond": 330,
        "diamond_axe": 330,
        "diamond_hoe": 330,
        "diamond_shovel": 330,
        "fireball": 320,
        "apple_golden": 320,
        "bucket_empty": 310,
        "bucket_lava": 310,
        "bucket_water": 310,
        "bucket_milk": 310,
        "anvil_base": 330,
        "anvil_top_damaged_0": 330,
        "anvil_top_damaged_1": 330,
        "anvil_top_damaged_2": 330,
        "bookshelf": 310,
        "bookshelf1 ": 310,
        "bookshelf2": 310,
        "bookshelf3 ": 310,
        "bookshelf4": 310,
        "brewing_stand": 320,
        "brick": 320,
        "brewing_stand_base": 320,
        "cauldron_side": 330,
        "cauldron_inner": 330,
        "cauldron_bottom": 330,
        "cauldron_top": 330,
        "hopper_inside": 330,
        "hopper_outside": 330,
        "hopper_top": 330,
        "lava_still": 310,
        "lava_flow": 310,
        "mushroom_block_inside": 315,
        "mushroom_block_skin_brown": 315,
        "soul_sand": 305,
        "slime": 300,
        "redstone_lamp_on": 310,
        "redstone_lamp_off": 310,
        "ice": 320,
        "ladder": 300,
        "ice_packed": 320,
        "netherrack": 310,
        "quartz_ore": 300,
        "redstone_block": 295,
        "mycelium_top": 320,
        "mycelium_side": 320,
        "stone_granite_smooth": 310,
        "stone_granite": 310,
        "stone_diorite_smooth": 315,
        "stone_diorite": 315,
        "gravel": 325
}

GRADIENT_MAP = {
    "colormap": ((255, 214, 231), (166, 0, 91)),
}

GUI_HUE_MAP = {
    "title": 330,
    "background": 330,
    "container": 330,
    "creative_inventory": 330,
    "demo_background": 330,
    "options_background": 330,
    "icons": 330
}
PARTICLE_HUE_MAP = {
    "particles": 345,
}
# === Extra Entity Maps ===
ENTITY_HUE_MAP = {
    "blaze": 330,
    "experience_orb": 330,
    "arrow": 290,
    "normal": 315,
    "normal_double": 315,
    "trapped": 315,
    "trapped_double": 315,
    "ender": 390,
    "enderman_eyes": 270,
    "enderman": 330
}


def process_entity_folder(base_entity_path, hue_map=None, gradient_map=None):
    for root, dirs, files in os.walk(base_entity_path):
        rel_path = os.path.relpath(root, base_entity_path)
        output_folder = os.path.join(OUTPUT_DIR, "entity", rel_path)
        os.makedirs(output_folder, exist_ok=True)

        for f in files:
            if not f.lower().endswith('.png'):
                continue

            input_path = os.path.join(root, f)
            output_path = os.path.join(output_folder, f)

            folder_name = os.path.basename(root)
            base_name = os.path.splitext(f)[0]

            hue = hue_map.get(base_name) or hue_map.get(folder_name)

            if hue is None and (not gradient_map or base_name not in gradient_map):
                print(f"Skipping unknown entity texture: {f}")
                continue

            with Image.open(input_path) as img:
                if hue is not None:
                    img = shift_hue(img, hue)
                elif gradient_map and base_name in gradient_map:
                    img = apply_gradient(img, *gradient_map[base_name])
                img.save(output_path)
                print(f"Processed entity: {f}")

# === Recolor Functions ===
def shift_hue(img, hue_deg):
    hue_shift = hue_deg / 360.0
    img = img.convert('RGBA')
    pixels = img.load()
    for y in range(img.height):
        for  x in range(img.width):
            r, g, b, a = pixels[x, y]
            if a == 0:
                continue
            h, s, v = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)
            h = hue_shift
            # boost very low v slightly so hue is visible
            if v < 0.1:
                v = 0.1
            r, g, b = colorsys.hsv_to_rgb(h, s, v)
            pixels[x, y] = (int(r * 255), int(g * 255), int(b * 255), a)
    return img

def apply_gradient(img, start_color, end_color):
    img = img.convert('RGBA')
    pixels = img.load()
    width = img.width
    for x in range(width):
        t = x / (width - 1) if width > 1 else 0
        r = int(start_color[0] + (end_color[0] - start_color[0]) * t)
        g = int(start_color[1] + (end_color[1] - start_color[1]) * t)
        b = int(start_color[2] + (end_color[2] - start_color[2]) * t)
        for y in range(img.height):
            _, _, _, a = pixels[x, y]
            pixels[x, y] = (r, g, b, a)
    return img

# === Processing Function ===
def process_folder(folder_path, hue_map=None, gradient_map=None):
    for root, dirs, files in os.walk(folder_path):
        rel_path = os.path.relpath(root, folder_path)
        output_folder = os.path.join(OUTPUT_DIR, rel_path)
        os.makedirs(output_folder, exist_ok=True)

        for f in files:
            if not f.lower().endswith('.png'):
                continue

            input_path = os.path.join(root, f)
            output_path = os.path.join(output_folder, f)

            folder_name = os.path.basename(root)
            base_name = os.path.splitext(f)[0]

            hue = None
            grad = None

            if hue_map:
                hue = hue_map.get(folder_name) or hue_map.get(base_name)

            if gradient_map:
                grad = gradient_map.get(folder_name) or gradient_map.get(base_name)

            if hue is None and grad is None:
                print(f"Skipping unknown: {f}")
                continue

            with Image.open(input_path) as img:
                if hue is not None:
                    img = shift_hue(img, hue)
                elif grad is not None:
                    img = apply_gradient(img, *grad)
                img.save(output_path)
                print(f"Processed {f}")

# === Main ===
if __name__ == "__main__":
    print("Processing variant folders...")
    process_folder(INPUT_DIR, VARIANT_HUE_MAP)

    print("Processing items...")
    process_folder(INPUT_DIR, ITEM_HUE_MAP)

    print("Processing gradients...")
    process_folder(INPUT_DIR, gradient_map=GRADIENT_MAP)

    print("Processing GUI...")
    process_folder(INPUT_DIR, GUI_HUE_MAP)

    print("Processing particles...")
    process_folder(INPUT_DIR, PARTICLE_HUE_MAP)

    print("Processing entities...")
    ENTITY_DIR = os.path.join(INPUT_DIR, "entity")
    process_entity_folder(ENTITY_DIR, hue_map=ENTITY_HUE_MAP)

    print("✅ All recoloring done!")