import allure


class Test_002:

    def test_add_png(self):
        print("--->test_add_png")
        with open("./img/abc.png", "rb") as f:
            print("f:",f)
            allure.attach("截图", f.read(), allure.attach_type.png)
        assert True
