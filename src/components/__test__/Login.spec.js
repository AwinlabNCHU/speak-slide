import { mount } from "@vue/test-utils";
import Login from "../Login.vue";

describe("Login.vue", () => {
  it("renders login form", () => {
    const wrapper = mount(Login);
    expect(wrapper.text()).toContain("Sign in to your account");
  });

  it("shows error if fields are empty", async () => {
    const wrapper = mount(Login);
    await wrapper.find("form").trigger("submit.prevent");
    expect(wrapper.text()).toContain("required");
  });

  // You can mock axios and test API call logic as well
});
r