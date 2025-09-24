document.addEventListener("DOMContentLoaded", () => {
  //Lógica do menu hamburguer
  let isOpen = true;
  const menuHamb = document.querySelector(".menu-hamb");
  const menuHambToggle = document.querySelector(".menu-hamb-toggle");

  menuHambToggle.addEventListener("click", () => {
    if (isOpen) {
      menuHamb.classList.toggle("show");
    } else {
      menuHamb.classList.remove("show");
    }
    isOpen = !isOpen;
  });

  //Lógica do menu dropdown
  const dropdownToggles = document.querySelectorAll(".dropdown-toggle");

  function dropdown(action) {
    //Atribui a função aos menus
    dropdownToggles.forEach((toggle) => {
      toggle.addEventListener(action, function(e) {
        //Evita bugs ao clicar no menu
        e.stopPropagation();

        //Garante que o botão seja sempre o selecionado
        const button = e.currentTarget;
        const dropdownMenu =
          button.parentElement.querySelector(".dropdown-content");

        //Fecha os outros menus e deixa o selecionado aberto
        document.querySelectorAll(".dropdown-content").forEach((menu) => {
          if (menu !== dropdownMenu) {
            menu.classList.remove("show");
          }
        });

        //Remove o indicador visual dos menus não selecionados
        dropdownToggles.forEach((otherToggle) => {
          if (otherToggle !== button) {
            otherToggle.classList.remove("toggle-color");
          }
        });

        //Ativa e indica o menu selecionado
        dropdownMenu.classList.toggle("show");
        button.classList.toggle("toggle-color");
      });
    });

    document.addEventListener("click", () => {
      //Fecha todos os menus ao clicar fora
      document.querySelectorAll(".dropdown-content").forEach((menu) => {
        menu.classList.remove("show");
      });

      //Remove a indicação visual de todos os menus
      dropdownToggles.forEach((otherToggle) => {
        otherToggle.classList.remove("toggle-color");
      });
    });
  }

  //Verifica o tamanho da tela e atribui um evento
  if (window.innerWidth <= 768) {
    dropdownToggles.forEach((toggle) => {
      toggle.addEventListener("click", dropdown("click"));
    });
  } else {
    dropdownToggles.forEach((toggle) => {
      toggle.addEventListener("mouseenter", dropdown("mouseenter"));
    });
  }
});