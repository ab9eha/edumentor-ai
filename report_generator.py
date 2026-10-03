from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    HRFlowable
)

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.units import mm


def create_report(
    filename,
    name,
    subject,
    score,
    status,
    recommendation
):

    # ---------------------------------------------------------
    # DOCUMENT SETUP
    # ---------------------------------------------------------

    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        rightMargin=22 * mm,
        leftMargin=22 * mm,
        topMargin=20 * mm,
        bottomMargin=20 * mm
    )

    styles = getSampleStyleSheet()

    # ---------------------------------------------------------
    # CUSTOM STYLES
    # ---------------------------------------------------------

    title_style = ParagraphStyle(
        "MainTitle",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=28,
        leading=34,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#172554"),
        spaceAfter=8
    )

    subtitle_style = ParagraphStyle(
        "Subtitle",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=12,
        leading=18,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#475569"),
        spaceAfter=5
    )

    report_title_style = ParagraphStyle(
        "ReportTitle",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=17,
        leading=22,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#1E3A8A"),
        spaceAfter=10
    )

    section_style = ParagraphStyle(
        "Section",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=13,
        leading=18,
        textColor=colors.HexColor("#172554"),
        spaceAfter=8
    )

    body_style = ParagraphStyle(
        "Body",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=10.5,
        leading=17,
        textColor=colors.HexColor("#334155")
    )

    center_body_style = ParagraphStyle(
        "CenterBody",
        parent=body_style,
        alignment=TA_CENTER
    )

    score_style = ParagraphStyle(
        "Score",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=30,
        leading=35,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#1E40AF")
    )

    status_style = ParagraphStyle(
        "Status",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=15,
        leading=20,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#166534")
    )

    small_style = ParagraphStyle(
        "Small",
        parent=body_style,
        fontSize=9,
        leading=13,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#64748B")
    )

    # ---------------------------------------------------------
    # CONTENT
    # ---------------------------------------------------------

    content = []

    # Top spacing
    content.append(Spacer(1, 20))

    # Small professional brand mark
    content.append(
        Paragraph(
            "EDUMENTOR AI",
            ParagraphStyle(
                "Brand",
                parent=styles["Normal"],
                fontName="Helvetica-Bold",
                fontSize=10,
                leading=14,
                alignment=TA_CENTER,
                textColor=colors.HexColor("#2563EB"),
                spaceAfter=12
            )
        )
    )

    # Main title
    content.append(
        Paragraph(
            "EduMentor AI",
            title_style
        )
    )

    # Subtitle
    content.append(
        Paragraph(
            "Personalized Learning & Performance Platform",
            subtitle_style
        )
    )

    content.append(Spacer(1, 14))

    # Divider
    content.append(
        HRFlowable(
            width="65%",
            thickness=1,
            color=colors.HexColor("#CBD5E1"),
            spaceBefore=5,
            spaceAfter=18,
            hAlign="CENTER"
        )
    )

    # Report title
    content.append(
        Paragraph(
            "PERSONALIZED LEARNING REPORT",
            report_title_style
        )
    )

    content.append(
        Paragraph(
            "A summary of your learning activity, quiz performance, "
            "and recommended next steps.",
            center_body_style
        )
    )

    content.append(Spacer(1, 25))

    # ---------------------------------------------------------
    # STUDENT INFORMATION
    # ---------------------------------------------------------

    content.append(
        Paragraph(
            "STUDENT INFORMATION",
            section_style
        )
    )

    student_data = [
        [
            Paragraph("<b>Student Name</b>", body_style),
            Paragraph(str(name), body_style)
        ],
        [
            Paragraph("<b>Subject</b>", body_style),
            Paragraph(str(subject), body_style)
        ],
        [
            Paragraph("<b>Learning Level</b>", body_style),
            Paragraph(
                "Personalized Learning",
                body_style
            )
        ]
    ]

    student_table = Table(
        student_data,
        colWidths=[55 * mm, 105 * mm],
        rowHeights=[12 * mm, 12 * mm, 12 * mm]
    )

    student_table.setStyle(
        TableStyle([
            (
                "BACKGROUND",
                (0, 0),
                (0, -1),
                colors.HexColor("#F1F5F9")
            ),
            (
                "BACKGROUND",
                (1, 0),
                (1, -1),
                colors.white
            ),
            (
                "BOX",
                (0, 0),
                (-1, -1),
                0.8,
                colors.HexColor("#CBD5E1")
            ),
            (
                "INNERGRID",
                (0, 0),
                (-1, -1),
                0.5,
                colors.HexColor("#E2E8F0")
            ),
            (
                "VALIGN",
                (0, 0),
                (-1, -1),
                "MIDDLE"
            ),
            (
                "LEFTPADDING",
                (0, 0),
                (-1, -1),
                12
            ),
            (
                "RIGHTPADDING",
                (0, 0),
                (-1, -1),
                12
            )
        ])
    )

    content.append(student_table)

    content.append(Spacer(1, 28))

    # ---------------------------------------------------------
    # PERFORMANCE SUMMARY
    # ---------------------------------------------------------

    content.append(
        Paragraph(
            "PERFORMANCE SUMMARY",
            section_style
        )
    )

    score_box = Table(
        [
            [
                Paragraph(
                    f"{score}%",
                    score_style
                )
            ],
            [
                Paragraph(
                    "Overall Quiz Score",
                    center_body_style
                )
            ]
        ],
        colWidths=[70 * mm],
        rowHeights=[20 * mm, 12 * mm]
    )

    score_box.setStyle(
        TableStyle([
            (
                "BACKGROUND",
                (0, 0),
                (-1, -1),
                colors.HexColor("#EFF6FF")
            ),
            (
                "BOX",
                (0, 0),
                (-1, -1),
                1,
                colors.HexColor("#BFDBFE")
            ),
            (
                "VALIGN",
                (0, 0),
                (-1, -1),
                "MIDDLE"
            ),
            (
                "LEFTPADDING",
                (0, 0),
                (-1, -1),
                10
            ),
            (
                "RIGHTPADDING",
                (0, 0),
                (-1, -1),
                10
            )
        ])
    )

    content.append(score_box)

    content.append(Spacer(1, 14))

    # Status
    content.append(
        Paragraph(
            str(status),
            status_style
        )
    )

    content.append(Spacer(1, 22))

    # ---------------------------------------------------------
    # RECOMMENDATION
    # ---------------------------------------------------------

    content.append(
        Paragraph(
            "AI LEARNING RECOMMENDATION",
            section_style
        )
    )

    recommendation_table = Table(
        [
            [
                Paragraph(
                    str(recommendation),
                    body_style
                )
            ]
        ],
        colWidths=[160 * mm]
    )

    recommendation_table.setStyle(
        TableStyle([
            (
                "BACKGROUND",
                (0, 0),
                (-1, -1),
                colors.HexColor("#F8FAFC")
            ),
            (
                "BOX",
                (0, 0),
                (-1, -1),
                0.8,
                colors.HexColor("#CBD5E1")
            ),
            (
                "LEFTPADDING",
                (0, 0),
                (-1, -1),
                14
            ),
            (
                "RIGHTPADDING",
                (0, 0),
                (-1, -1),
                14
            ),
            (
                "TOPPADDING",
                (0, 0),
                (-1, -1),
                12
            ),
            (
                "BOTTOMPADDING",
                (0, 0),
                (-1, -1),
                12
            )
        ])
    )

    content.append(recommendation_table)

    content.append(Spacer(1, 35))

    # ---------------------------------------------------------
    # FOOTER INFORMATION
    # ---------------------------------------------------------

    content.append(
        HRFlowable(
            width="100%",
            thickness=0.7,
            color=colors.HexColor("#CBD5E1"),
            spaceBefore=5,
            spaceAfter=12
        )
    )

    content.append(
        Paragraph(
            "EduMentor AI",
            ParagraphStyle(
                "FooterBrand",
                parent=styles["Normal"],
                fontName="Helvetica-Bold",
                fontSize=9,
                alignment=TA_CENTER,
                textColor=colors.HexColor("#334155")
            )
        )
    )

    content.append(
        Paragraph(
            "AI-assisted educational analytics and personalized learning support",
            small_style
        )
    )

    # ---------------------------------------------------------
    # BUILD PDF
    # ---------------------------------------------------------

    doc.build(content)