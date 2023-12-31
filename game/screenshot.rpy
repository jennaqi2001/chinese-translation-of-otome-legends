init 999 python:

    # Called to make a screenshot happen.
    def _custom_screenshot():
        import os.path
        import os
        import __main__

        if renpy.macapp:
            renpy.config.screenshot_folder = os.path.expanduser(b"~/Desktop")
        else:
            # define the new destination folder as game\screenshots
            renpy.config.screenshot_folder = os.path.join(config.gamedir, "screenshots")
            # check if the new destination folder already exists: if not, try to create it
            # if the new destination folder can't be created, fall back on the original destination
            if not os.path.exists(config.screenshot_folder):
                try:
                    os.makedirs(config.screenshot_folder)
                except:
                    config.screenshot_folder = config.renpy_base

        # Try to pick a filename.
        i = 1
        while True:
            fn = os.path.join(config.screenshot_folder, config.screenshot_pattern % i)
            if not os.path.exists(fn):
                break
            i += 1

        try:
            if not renpy.screenshot(fn):
                renpy.notify(__("Failed to save screenshot as %s.") % fn)
                return
        except:
            import traceback
            traceback.print_exc()
            renpy.notify(__("Failed to save screenshot as %s.") % fn)
            return

        if config.screenshot_callback is not None:
            config.screenshot_callback(fn)

    custom_keymap = renpy.Keymap(screenshot = _custom_screenshot)
    config.underlay.append(custom_keymap)
