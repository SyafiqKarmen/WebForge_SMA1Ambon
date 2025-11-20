import { LitElement, html, css } from "https://cdn.jsdelivr.net/npm/lit@3/bundled/lit.min.js";

class MyBox extends LitElement {
  static styles = css`
    div {
      color: white;
      background: #9b1b30;
      padding: 10px;
      border-radius: 8px;
    }
  `;

  render() {
    return html`
      <div>Hello from Lit!</div>
    `;
  }
}

customElements.define('my-box', MyBox);
