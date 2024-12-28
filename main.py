import flet as ft

def main(page: ft.Page):
    page.bgcolor = ft.colors.BLACK 
    page.scroll = ft.ScrollMode.AUTO
    
    def change_main_image(e):
        for elem in options.controls:
            if elem == e.control:
                elem.opacity = 1
                main_image.src = elem.image_src
            else:
                elem.opacity = 0.5
        main_image.update()
        options.update()    
    
    product_images = ft.Container(
        col={'xs': 12, 'md': 6},
        bgcolor=ft.colors.WHITE,
        padding=ft.padding.all(30),
        aspect_ratio=9/11,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                main_image := ft.Image(
                    src='Captura de tela 2024-12-22 145145.png',
                ),
                
                options :=ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            image_src='Captura de tela 2024-12-22 145145.png',
                            width=80,
                            height=80,
                            opacity=1,
                            on_click=change_main_image 
                            
                        ),
                        
                        ft.Container(
                            image_src='images (1).jpg',
                            width=80,
                            height=80,
                            opacity=1,
                            on_click=change_main_image 
                            
                        ),
                        
                        ft.Container(
                            image_src='images.jpg',
                            width=80,
                            height=80,
                            opacity=1,
                            on_click=change_main_image 
                            
                        ),
                    ]
                )
            ] 
            
            
        )
    
    )

    # Detalhes do produto (exemplo básico)
    product_details = ft.Container(
        col={'xs': 12, 'md': 6},
        padding=ft.padding.all(30),
        bgcolor=ft.colors.BLACK87,
        aspect_ratio=9/11,
        content=ft.Column(
            controls=[
                ft.Text(
                    value='CADEIRAS',
                    color=ft.colors.AMBER,
                    weight=ft.FontWeight.BOLD,
                ),
                
                ft.Text(
                    value='Poltrona Amarela Moderna',
                    color=ft.colors.WHITE,
                    weight=ft.FontWeight.BOLD,
                    size=30,
                ),
                
                ft.Text(value='Sala de estar', color=ft.colors.GREY, italic=True),
                
                ft.ResponsiveRow(
                    columns=12,
                    controls=[
                        ft.Text(  
                            col={'xs': 12, 'sm': 6 },    
                            value='R$ 399',
                            color=ft.colors.WHITE,
                            size=30,
                        ),
                        ft.Row(
                            col={'xs': 12, 'sm': 6 },
                            controls=[
                                ft.Icon(
                                    name=ft.cupertino_icons.STAR,
                                    color=ft.colors.AMBER if _ < 4 else ft.colors.WHITE, 
                                ) for _ in range(5)
                            ]
                        )
                    ]
                ),
                
                ft.Tabs(
                    selected_index=0,
                    height=150,
                    indicator_color=ft.colors.AMBER,
                    label_color=ft.colors.AMBER,
                    unselected_label_color=ft.colors.GREY,
                    tabs=[
                        ft.Tab(
                            text='Descrição',
                            content=ft.Container(
                                padding=ft.padding.all(10),
                                content=ft.Text(
                                    value='Com traços inusitados e combinação de diferentes materiais, a poltrona Lyric apresenta proporções equilibradas, com muito estilo e conforto. Sua estrutura é em tubo de aço carbono, com apoio posterior em chapa de aço revestido com lâmina natural de madeira, assento estofado fixo e almofada solta no encosto.',
                                    color=ft.colors.GREY,  
                                )   
                            )
                        ),
                        
                        ft.Tab(
                            text='Detalhes',
                             content=ft.Container(
                                padding=ft.padding.all(10),
                                content=ft.Text(
                                    value='Valores, preços e promoções, estão disponíveis aqui a todo momento. Venha e confira',
                                    color=ft.colors.GREY,  
                                )   
                            )
                        )
                    ]
                ),
                
                ft.ResponsiveRow(
                    columns=12,  
                    controls=[
                        ft.Dropdown(
                            col=6,
                            label='Cor',
                            label_style=ft.TextStyle(color=ft.colors.WHITE, size=16),
                            border_color=ft.colors.GREY,
                            border_width=0.5,
                            options=[
                                ft.dropdown.Option(text='Amarelo'),
                                ft.dropdown.Option(text='Vermelho'),
                                ft.dropdown.Option(text='Azul'),
                            ]
                            
                        ),
                        
                        ft.Dropdown(
                            col=6,
                            label='Quantidade',
                            label_style=ft.TextStyle(color=ft.colors.WHITE, size=16),
                            border_color=ft.colors.GREY,
                            border_width=0.5,
                            options=[
                                ft.dropdown.Option(text=f'{num} unid.') for num in range(1, 11)
                                
                            ]
                            
                        )
                    ]
                ),
                
                ft.Container(expand=True),
                
                ft.ElevatedButton(
                    width=900,
                    text='Adicionar a lista de desejos',
                    style=ft.ButtonStyle(
                        padding=ft.padding.all(20),
                        side={
                            ft.MaterialState.DEFAULT: ft.BorderSide(width=2, color=ft.colors.WHITE)
                        },
                        bgcolor={
                            ft.MaterialState.HOVERED: ft.colors.BLACK,
                        },
                        color={
                            ft.MaterialState.DEFAULT: ft.colors.BLACK,
                            ft.MaterialState.HOVERED: ft.colors.WHITE,
                        }
                    )
                ),
                
                ft.ElevatedButton(
                    width=900,
                    text='Adicionar ao carrinho',
                    style=ft.ButtonStyle(
                        padding=ft.padding.all(20),
                        side={
                            ft.MaterialState.DEFAULT: ft.BorderSide(width=2, color=ft.colors.AMBER)
                        },
                        bgcolor={
                            ft.MaterialState.HOVERED: ft.colors.BLACK,  
                        },
                        color={
                            ft.MaterialState.DEFAULT: ft.colors.BLACK,
                            ft.MaterialState.HOVERED: ft.colors.AMBER,
                        }
                    )
                )
            ]
        )
    )
    
    layout = ft.Container(
        width=900,
        margin=ft.margin.all(30),
        shadow=ft.BoxShadow(blur_radius=300, color=ft.colors.CYAN),
        content=ft.ResponsiveRow(
            columns=10,
            spacing=0,
            run_spacing=0,
            controls=[
                product_images,
                product_details,
            ]
        
        )
        
    )

    # Layout principal usando Row para alinhar os contêineres
    
        

    # Adicionando o layout à página
    page.add(layout)

# Bloco principal
if __name__ == '__main__':
    ft.app(target=main)
    
